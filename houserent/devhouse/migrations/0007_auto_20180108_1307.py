# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-08 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devhouse', '0006_auto_20180108_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devinfo',
            name='dev_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='搜集時間'),
        ),
    ]
