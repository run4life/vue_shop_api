# -*- coding:utf-8 -*-
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=36, unique=True)
    password = models.CharField(max_length=36)
    rid = models.IntegerField(null=True)
    mobile = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    state = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    delete_time = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    rid = models.IntegerField(null=True)
    role_name = models.CharField(max_length=36, unique=True)
    ids = models.CharField(max_length=512)
    controler_action = models.TextField(blank=True, null=True)
    role_desc = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    delete_time = models.DateTimeField(auto_now_add=True)

class Right(models.Model):
    name = models.CharField(max_length=36, unique=True)
    pid = models.IntegerField(null=True)
    controler = models.CharField(max_length=36)
    action = models.CharField(max_length=36)
    level = models.SmallIntegerField(choices=(('1','一级'),('2','二级'),('3','三级')),default=1)
    deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    delete_time = models.DateTimeField(auto_now_add=True)

class RightApi(models.Model):
    right_id = models.CharField(max_length=255)
    right_id_service = models.CharField(max_length=255)
    right_api_action = models.CharField(max_length=255)
    right_api_order = models.IntegerField()