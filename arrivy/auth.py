import datetime
import jwt

SECRET_KEY = 'verysecret'


def generate_access_token(user):
    access_token_payload = {
        'user_email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=100),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, SECRET_KEY, algorithm='HS256')

    return refresh_token
