# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 02:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping_List', '0008_auto_20171202_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery_list',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
