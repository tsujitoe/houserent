# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devhouse', '0022_auto_20180123_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='devinfo',
            name='dev_screenshot_yes',
            field=models.BooleanField(default=False, verbose_name='有截過圖嗎?'),
        ),
    ]