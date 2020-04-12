#-- coding:UTF-8 --
from backend.extensions.auth import JwtQueryParamsAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from backend import models
from backend.utils.encryption import encrypt, decrypt




class RightsView(APIView):
    def get(self, request, type):     
        if type == "list":
            right_objects = models.Right.objects.all().order_by("id") 
            returndata = {}
            data = {}
            meta = {}
            rightlist = []
            for right in right_objects:
                rightdict = {}
                rightdict['id'] = right.id
                rightdict['authName'] = right.name
                rightdict['level'] = right.level
                rightdict['pid'] = right.pid
                rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                rightlist.append(rightdict)
            data = rightlist
            returndata['data'] = data
            meta['msg'] = '查询成功'
            meta['status'] = 200
            returndata['meta'] = meta
            return Response(returndata)
        
        if type == "tree":
            right_objects = models.Right.objects.all().order_by("id") 
            returndata = {}
            data = {}
            meta = {}
            rightresult = {}
            for right in right_objects:
                if right.level == 0:
                    rightdict = {}
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
                    rightdict['id'] = right.id
                    rightdict['authName'] = right.name
                    rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                    ppid = tmpresult[right.pid]['pid']
                    rightdict['pid'] = str(right.pid) + ',' + str(ppid)
                    for prentrightresult in rightresult[ppid]['children']:
                        if prentrightresult['id'] == right.pid:
                            prentrightresult['children'].append(rightdict)
            #rightresult[ppid]['children'].append(prentrightresult)
            data = rightresult.values()
            returndata['data'] = data
            meta['msg'] = '查询成功'
            meta['status'] = 200
            returndata['meta'] = meta

            return Response(returndata)

class MenusView(APIView):
    def get(self, request): 
        user_id = request.user.get('id')
        user_rid = request.user.get('rid')
        user_rights_object = models.Role.objects.filter(id = user_rid).first()
        
        if user_rights_object.ids is not None:
            user_rights = user_rights_object.ids.split(',')

        right_objects = models.Right.objects.all().order_by("id") 
        returndata = {}
        data = {}
        meta = {}
        rightresult = {}
        for right in right_objects:
            if right.level == 0:
                rightdict = {}
                rightdict['id'] = right.id
                if str(rightdict['id']) not in user_rights:
                    continue
                rightdict['authName'] = right.name
                rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                rightdict['pid'] = right.pid
                rightdict['children'] = []
                rightresult[right.id] = rightdict
            
        tmpresult = {}
        for right in right_objects:
            if right.level == 1:
                rightdict = {}
                rightdict['id'] = right.id
                if str(rightdict['id']) not in user_rights:
                    continue
                rightdict['authName'] = right.name
                rightdict['path'] = models.RightApi.objects.filter(right_id=right.id).first().right_api_path
                rightdict['pid'] = right.pid
                rightdict['children'] = []
                tmpresult[right.id] = rightdict
                rightresult[right.pid]['children'].append(tmpresult[right.id])

        data = rightresult.values()

        returndata['data'] = data
        meta['msg'] = '查询成功'
        meta['status'] = 200
        returndata['meta'] = meta

        return Response(returndata)