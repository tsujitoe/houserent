# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostreet', '0006_auto_20180117_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediainfo',
            name='now_note',
            field=models.TextField(blank=True, default='租金價位: \n是否仲介: \n其他注意:', null=True, verbose_name='紀錄備忘'),
        ),
    ]
