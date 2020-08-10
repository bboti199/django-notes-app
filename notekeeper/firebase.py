import os
from firebase_admin import auth, credentials, initialize_app
from . import exceptions
from .models import User
from notekeeper_django.settings import BASE_DIR

from rest_framework import authentication

cred = credentials.Certificate(os.path.join(BASE_DIR, os.environ.get('FIREBASE_ADMIN_PATH')))

firebase_app = initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            raise exceptions.NoAuthToken('No authentication token provided')

        id_token = auth_header.split(' ').pop()
        decoded_token = None

        if not id_token:
            return None

        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise exceptions.InvalidToken("Invalid auth token")

        if not decoded_token:
            return None

        try:
            uid = decoded_token.get('uid')
            email = decoded_token.get('email')
        except Exception:
            raise exceptions.FirebaseError()

        user, created = User.objects.get_or_create(fid=uid, email=email)

        return user, None
