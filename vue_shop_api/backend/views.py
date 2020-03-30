# -*- coding:utf-8 -*-
import subprocess
from django.http import HttpResponse
from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeListSerializer, CodeSerializer
from .models import Code
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    去除 CSRF 检查
    """

    def enforce_csrf(self, request):
        return

class CodeViewSet(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def list(self, request, *args, **kwargs):
        """
        使用专门的列表序列化器，而非默认的序列化器
        """
        serializer = CodeListSerializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def run_create_or_update(self, request, serializer):
        """
        create 和 update 的共有逻辑，仅仅是简单的多了 run 参数的判断
        """
        if serializer.is_valid():
            code = serializer.validated_data.get('code')
            serializer.save()
            if 'run' in request.query_params.keys():
                output = self.run_code(code)
                data = serializer.data
                data.update({'output': output})
                return Response(data=data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        return self.run_create_or_update(request, serializer)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        return self.run_create_or_update(request, serializer)
