# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-10 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devhouse', '0010_auto_20180110_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devinfo',
            name='dev_url',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='網址'),
        ),
    ]
