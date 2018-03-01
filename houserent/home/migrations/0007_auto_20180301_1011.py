# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180228_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinfo',
            name='home_partten',
            field=models.CharField(default=' 房 廳 衛 陽台', max_length=50, verbose_name='格局'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_rent',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='租金'),
        ),
    ]
