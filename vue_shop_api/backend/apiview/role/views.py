#-- coding:UTF-8 --
from backend.extensions.auth import JwtQueryParamsAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from backend import models



class RolesView(APIView):

    def get(self, request):
        role_objects = models.Role.objects.filter(deleted=False).order_by("id")
        
        returndata = {}
        meta = {}
        roles = []
        for role_object in role_objects:
            role_dict = {}
            role_dict['id'] = role_object.id
            role_dict['roleName'] = role_object.role_name
            role_dict['roleDesc'] = role_object.role_desc
            role_dict['children'] = []
            roles.append(role_dict)
            #如果用户创建后，未配置角色属性判断
            if role_object.ids is not None:
                role_rights = role_object.ids.split(',')
            else:
                role_dict['children'] = []
                continue
            
            right_objects = models.Right.objects.all().order_by("id") 
            returndata = {}
            data = {}
            meta = {}
            rightresult = {}
            for right in right_objects:
                if right.level == 0:
                    rightdict = {}
                    if str(right.id) not in role_rights:
                        continue
                    rightdict['id'] = right.id
                    rightdict['authName'] = right.name
                    rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                    rightdict['pid'] = right.pid
                    rightdict['children'] = []
                    rightresult[right.id] = rightdict
            
            tmpresult = {}
            for right in right_objects:
                if right.level == 1:
                    rightdict = {}
                    if str(right.id) not in role_rights:
                        continue
                    rightdict['id'] = right.id
                    rightdict['authName'] = right.name
                    rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                    rightdict['pid'] = right.pid
                    rightdict['children'] = []
                    tmpresult[right.id] = rightdict
                    rightresult[right.pid]['children'].append(tmpresult[right.id])

            
            for right in right_objects:
                if right.level == 2:
                    rightdict = {}
                    if str(right.id) not in role_rights:
                        continue
                    rightdict['id'] = right.id
                    rightdict['authName'] = right.name
                    rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                    ppid = tmpresult[right.pid]['pid']
                    rightdict['pid'] = str(right.pid) + ',' + str(ppid)
                    for prentrightresult in rightresult[ppid]['children']:
                        if prentrightresult['id'] == right.pid:
                            prentrightresult['children'].append(rightdict)
            role_dict['children'] = rightresult.values()

        meta['msg'] = '获取用户列表成功'
        meta['status'] = 200
        returndata['data'] = roles
        returndata['meta'] = meta

        return Response(returndata,status=200)
    
    def post(self, request):
        rolename = request.data.get('roleName')
        roledesc = request.data.get('roleDesc')

        role_object = models.Role(
            role_name = rolename,
            role_desc = roledesc
        )
        role_object.save()
        
        returndata = {}
        data = {}
        meta = {}
        data['roleId'] = role_object.id
        data['roleName'] = role_object.role_name
        data['roleDesc'] = role_object.role_desc
 
        meta['msg'] = '用户角色成功'
        meta['status'] = 201
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=201)


class RoleView(APIView):
    
    def get(self, request, role_id):
        role_object = models.Role.objects.filter(id=role_id, deleted=False).first()
        if not role_object:
            returndata = {}
            meta = {}
            meta['msg'] = '角色不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)

        returndata = {}
        data = {}
        meta = {}
        data['roleId'] = role_object.id
        data['roleName'] = role_object.role_name
        data['roleDesc'] = role_object.role_desc
        meta['msg'] = '查询成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)
    
    def put(self, request, role_id):
        rolename = request.data.get('roleName')
        roledesc = request.data.get('roleDesc')
        role_object = models.Role.objects.filter(id=role_id, deleted=False).first()
        if not role_object:
            returndata = {}
            meta = {}
            meta['msg'] = '角色不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)
        role_object.role_name = rolename
        role_object.role_desc = roledesc
        role_object.save()
        returndata = {}
        data = {}
        meta = {}
        data['roleId'] = role_object.id
        data['roleName'] = role_object.role_name
        data['roleDesc'] = role_object.role_desc
        meta['msg'] = '角色编辑成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)

    def delete(self, request, role_id):
        role_object = models.Role.objects.filter(id=role_id, deleted=False).first()
        if not role_object:
            returndata = {}
            meta = {}
            meta['msg'] = '角色不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)
        role_object.deleted = True
        role_object.save()
        returndata = {}
        data = {}
        meta = {}
        meta['msg'] = '角色删除成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)

class RoleRightView(APIView):
    def post(self, request, role_id):
        rids = request.data.get('rids')
        role_object = models.Role.objects.filter(id=role_id, deleted=False).first()
        if not role_object:
            returndata = {}
            meta = {}
            meta['msg'] = '角色不存在'
            meta['status'] = 500
            returndata['meta'] = meta
            return Response(returndata,status=500)
        role_object.ids = rids
        role_object.save()
        
        returndata = {}
        data = {}
        meta = {}
 
        meta['msg'] = '角色权限更新成功'
        meta['status'] = 200
        returndata['data'] = data
        returndata['meta'] = meta
        return Response(returndata,status=200)