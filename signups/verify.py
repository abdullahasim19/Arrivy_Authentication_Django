import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from signups.ndbModels import User
from google.cloud import ndb

SECRET_KEY = 'verysecret'
class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        client=ndb.Client()
        with client.context():
            user = User.query(User.email == payload['user_email']).get()
            if user is None:
                raise exceptions.AuthenticationFailed('User not found')


        return user, None

