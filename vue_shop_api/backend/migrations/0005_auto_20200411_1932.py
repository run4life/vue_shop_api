# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-11 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200411_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='ids',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]