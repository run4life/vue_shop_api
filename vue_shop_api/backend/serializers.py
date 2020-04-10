# -*- coding:utf-8 -*-
from rest_framework import serializers

#创建序列化器
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    time = serializers.DateTimeField()
    rid = serializers.IntegerField()
    mobile = serializers.CharField()
    email = serializers.CharField()
    state = serializers.IntegerField()