# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gostreet.models


class Migration(migrations.Migration):

    dependencies = [
        ('gostreet', '0008_auto_20180118_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='street_images'
                , verbose_name='現場照片'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_files',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img_address', to='gostreet.MediaInfo'),
        ),
    ]
