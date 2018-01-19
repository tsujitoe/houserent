# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostreet', '0011_auto_20180118_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='image_note',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='照片說明'),
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='street_photo/%Y-%m-%d', verbose_name=''),
        ),
    ]
