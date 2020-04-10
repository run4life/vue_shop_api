#-- coding:UTF-8 --
from backend.extensions.auth import JwtQueryParamsAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from backend import models
from backend.utils.encryption import encrypt, decrypt




class RightsView(APIView):
    def get(self):
        pass



class RightView(APIView):
    def get(self):
        pass