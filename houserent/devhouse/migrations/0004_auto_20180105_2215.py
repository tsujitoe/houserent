# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-05 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devhouse', '0003_devinfo_dev_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devinfo',
            name='dev_tracetime',
            field=models.DateField(blank=True, null=True, verbose_name='追蹤時間'),
        ),
    ]