# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gostreet', '0005_auto_20180117_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediainfo',
            name='title',
        ),
        migrations.AddField(
            model_name='mediainfo',
            name='now_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='場勘地址'),
        ),
        migrations.AddField(
            model_name='mediainfo',
            name='now_note',
            field=models.TextField(blank=True, default='何時入住: \n預算多少: \n其他需求:', null=True, verbose_name='紀錄備忘'),
        ),
        migrations.AddField(
            model_name='mediainfo',
            name='now_phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='現場電話'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_files',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img_title', to='gostreet.MediaInfo'),
        ),
    ]