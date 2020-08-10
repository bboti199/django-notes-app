import os
from firebase_admin import auth, credentials, initialize_app
from . import exceptions
from .models import User
from notekeeper_django.settings import BASE_DIR

from rest_framework import authentication

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.environ.get('FB_PROJECT_ID'),
    "private_key_id": os.environ.get('FB_PRIVATE_KEY_ID'),
    "private_key": os.environ.get('FB_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('FB_CLIENT_EMAIL'),
    "client_id": os.environ.get('FB_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get('FB_CLIENT_X509_CERT_URL'),
})

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
