# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-11 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='delete_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='delete_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
