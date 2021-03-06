# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gostreet.models


class Migration(migrations.Migration):

    dependencies = [
        ('gostreet', '0002_auto_20180116_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images_street',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='images_street',
            name='img_street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img_street', to='gostreet.Post', verbose_name='案件地址'),
        ),
        migrations.AddField(
            model_name='post',
            name='street_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='images_street',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='street_images', verbose_name='掃街照片'),
        ),
    ]
