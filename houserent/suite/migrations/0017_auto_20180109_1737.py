# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-09 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0016_auto_20180108_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_number',
            field=models.CharField(default='X', max_length=10, verbose_name='房號'),
        ),
    ]
