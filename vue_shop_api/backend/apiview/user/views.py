#-- coding:UTF-8 --
from backend.extensions.auth import JwtQueryParamsAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from backend import models
from backend.utils.encryption import encrypt, decrypt

class UsersView(APIView):
    #authentication_classes = [JwtQueryParamsAuthentication]
    def get(self, request, *args, **kwargs):
        return Response('用户列表')
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        mobile = request.data.get('mobile')
        newpassword = encrypt(password)
        user_object = models.User(
            username = username,
            password = newpassword,
            mobile = mobile,
            email = email,
            state = False
            )
        user_object.save()

        returndata = {}
        data = {}
        meta = {}
        data['id'] = user_object.id
        data['role_id'] = user_object.rid
        data['username'] = user_object.username
        data['mobile'] = user_object.mobile
        data['email'] = user_object.email
        meta['msg'] = '用户创建成功'
        meta['status'] = 201
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=201)
    

class UserView(APIView):
    
    def get(self, request, user_id):
        user_object = models.User.objects.filter(id=user_id, deleted=False).first()
        if not user_object:
            returndata = {}
            meta = {}
            meta['msg'] = '用户不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)
        returndata = {}
        data = {}
        meta = {}
        data['id'] = user_object.id
        data['role_id'] = user_object.rid
        data['username'] = user_object.username
        data['mobile'] = user_object.mobile
        data['email'] = user_object.email
        meta['msg'] = '查询成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)
    
    def put(self, request, user_id):
        email = request.data.get('email')
        mobile = request.data.get('mobile')
        user_object = models.User.objects.filter(id=user_id, deleted=False).first()
        if not user_object:
            returndata = {}
            meta = {}
            meta['msg'] = '用户不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)
        user_object.email = email
        user_object.mobile = mobile
        user_object.save()
        returndata = {}
        data = {}
        meta = {}
        data['id'] = user_object.id
        data['role_id'] = user_object.rid
        data['username'] = user_object.username
        data['mobile'] = user_object.mobile
        data['email'] = user_object.email
        meta['msg'] = '用户修改成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)
    
    def delete(self, request, user_id):
        user_object = models.User.objects.filter(id=user_id, deleted=False).first()
        if not user_object:
            returndata = {}
            meta = {}
            meta['msg'] = '用户不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)
        user_object.deleted = True
        user_object.save()
        returndata = {}
        data = {}
        meta = {}
        meta['msg'] = '用户删除成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)