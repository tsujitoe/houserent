# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180228_0201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeinfo',
            options={'verbose_name_plural': '住宅案件'},
        ),
        migrations.AlterField(
            model_name='homemediainfo',
            name='home_title',
            field=models.CharField(max_length=60, verbose_name='標題'),
        ),
    ]