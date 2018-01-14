# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devstreet', '0005_remove_picture_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_image', models.ImageField(null=True, upload_to='dev-phone', verbose_name='現場照')),
            ],
        ),
        migrations.CreateModel(
            name='GoStreet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_address', models.CharField(max_length=100)),
                ('go_phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='goimage',
            name='go_street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='street', to='devstreet.GoStreet'),
        ),
    ]
