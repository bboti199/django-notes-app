from rest_framework import status
from rest_framework.exceptions import APIException


class NoAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = 'no_auth_token'
    default_detail = 'No authentication token provided'


class InvalidToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = 'invalid_token'
    default_detail = 'Invalid token provided'


class FirebaseError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = 'invalid_user'
    default_detail = 'Invalid firebase user'
