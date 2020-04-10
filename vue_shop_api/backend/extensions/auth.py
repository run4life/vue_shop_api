#-- coding:UTF-8 --
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from jwt import exceptions


class JwtQueryParamsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        tokenlist = token.split()
        token = tokenlist[1]
        salt = settings.SECRET_KEY
        payload = None
        msg = None
        try:
            payload = jwt.decode(token, salt, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'code':1003,'error':"token已失效"})
        except jwt.DecodeError:
            raise AuthenticationFailed({'code':1003,'error':"token认证失败"})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({'code':1003,'error':"非法的token"})
        return (payload, token)
        