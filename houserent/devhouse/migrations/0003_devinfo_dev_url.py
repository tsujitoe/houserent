# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-05 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devhouse', '0002_auto_20180105_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='devinfo',
            name='dev_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='網址'),
        ),
    ]
