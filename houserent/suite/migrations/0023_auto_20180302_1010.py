# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0022_auto_20180302_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suite',
            name='suite_fee_note',
            field=models.TextField(default='管理費： \n電費： \n水費： \n其他： ', verbose_name='雜費補充'),
        ),
        migrations.AlterField(
            model_name='suite',
            name='suite_note',
            field=models.TextField(default='如何進入大門： \n管理方式： \n垃圾處理： \n其他限制問題： \n', verbose_name='補充資訊'),
        ),
    ]
