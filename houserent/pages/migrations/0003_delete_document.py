# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-03 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180102_1819'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
