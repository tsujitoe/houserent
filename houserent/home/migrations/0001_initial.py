# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeMediaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_title', models.CharField(default='%Y-%m-%d-', max_length=60, verbose_name='標題')),
            ],
            options={
                'verbose_name_plural': '照片資訊',
            },
        ),
        migrations.CreateModel(
            name='HomePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_image', models.FileField(blank=True, null=True, upload_to='home_photo/%Y-%m-%d', verbose_name='照片')),
                ('h_date', models.DateTimeField(auto_now_add=True)),
                ('h_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo', to='home.HomeMediaInfo', verbose_name='標題')),
            ],
            options={
                'verbose_name_plural': '住宅照片',
            },
        ),
    ]
