# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtenant', '0002_auto_20180114_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tenant',
            options={'verbose_name_plural': '房客資訊'},
        ),
        migrations.AlterField(
            model_name='tenant',
            name='te_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='te_note',
            field=models.TextField(blank=True, default='何時入住: ', null=True, verbose_name='房客紀錄'),
        ),
    ]
