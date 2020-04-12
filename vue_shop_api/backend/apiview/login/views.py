#-- coding:UTF-8 --
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.utils.jwt_auth import create_token
from backend import models
from backend.serializers import UserSerializer
from backend.utils.encryption import encrypt, decrypt

import json


class LoginView(APIView):

    authentication_classes = []

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')
        newpwd = encrypt(pwd)
        user_object = models.User.objects.filter(username=user, password=newpwd, deleted=False).first()
        if not user_object:
            returndata = {}
            meta = {}
            meta['msg'] = '登录失败'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)

        token = create_token({'id': user_object.id, 'name': user_object.username, 'rid': user_object.rid})
        returndata = {}
        data = {}
        meta = {}
        data['id'] = user_object.id
        data['rid'] = user_object.rid
        data['username'] = user_object.username
        data['mobile'] = user_object.mobile
        data['email'] = user_object.email
        data['token'] = token
        meta['msg'] = '登录成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)
