# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-22 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostreet', '0019_auto_20180122_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeinfo',
            name='fake_source',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='來源'),
        ),
        migrations.AlterField(
            model_name='fakeinfo',
            name='fake_tenant',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='認養人'),
        ),
    ]
