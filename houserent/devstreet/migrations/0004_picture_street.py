# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-12 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devstreet', '0003_auto_20180112_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='地址'),
        ),
    ]
