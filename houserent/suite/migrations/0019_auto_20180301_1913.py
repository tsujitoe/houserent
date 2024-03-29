# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0018_auto_20180228_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suites',
            name='suite_limit',
        ),
        migrations.RemoveField(
            model_name='suites',
            name='suite_no_include',
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_fee_note',
            field=models.TextField(default=' | 管理費： \n | 電費： \n | 水費： \n | 其他： ', verbose_name='雜費補充'),
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_master',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='房東姓名'),
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_master_phone',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='房東電話'),
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_people_limit',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('學生', '學生'), ('家庭', '家庭'), ('上班族', '上班族'), ('禁男', '禁男'), ('禁女', '禁女'), ('禁小孩', '禁小孩'), ('禁拜拜', '禁拜拜'), ('禁煮飯', '禁煮飯'), ('請看補充資訊', '請看補充資訊')], max_length=100, null=True, verbose_name='身份限制'),
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_pet_limit',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('可寵', '可寵'), ('可貓', '可貓'), ('可狗', '可狗'), ('全部禁寵', '全部禁寵'), ('請看補充資訊', '請看補充資訊')], max_length=100, null=True, verbose_name='寵物限制'),
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_type',
            field=models.CharField(blank=True, choices=[('大樓', '大樓'), ('公寓', '公寓'), ('透天', '透天'), ('其他', '其他')], max_length=20, null=True, verbose_name='型態'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_address',
            field=models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='案件地址'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_drink',
            field=models.CharField(blank=True, choices=[('公共', '公共'), ('無', '無'), ('請看補充資訊', '請看補充資訊')], max_length=20, null=True, verbose_name='飲水'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_garbage',
            field=models.CharField(blank=True, choices=[('社區集中', '社區集中'), ('子母車', '子母車'), ('自理', '自理'), ('請看補充資訊', '請看補充資訊')], max_length=20, null=True, verbose_name='垃圾處理'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_how_inter_housedoor',
            field=models.CharField(choices=[('公司Key', '公司Key'), ('屋主開門', '屋主開門'), ('管理室', '管理室'), ('密碼', '密碼'), ('請看補充資訊', '請看補充資訊')], max_length=50, verbose_name='大門如何進入'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_how_inter_roomdoor',
            field=models.CharField(choices=[('公司Key', '公司Key'), ('屋主開門', '屋主開門'), ('管理室', '管理室'), ('藏在現場', '藏在現場'), ('沒鎖', '沒鎖'), ('密碼', '密碼'), ('請看補充資訊', '請看補充資訊')], max_length=50, verbose_name='房門如何進入'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_include',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('水', '水'), ('網路', '網路'), ('第四台', '第四台'), ('垃圾費', '垃圾費'), ('管理費', '管理費'), ('其他', '其他')], max_length=100, null=True, verbose_name='包含雜費'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_note',
            field=models.TextField(default=' | 如何進入大門： \n | 管理方式： \n | 垃圾處理： \n | 其他限制問題： \n', verbose_name='補充資訊'),
        ),
        migrations.AlterField(
            model_name='suites',
            name='suite_wash',
            field=models.CharField(blank=True, choices=[('獨立', '獨立'), ('公用', '公用'), ('無', '無'), ('請看補充資訊', '請看補充資訊')], max_length=20, null=True, verbose_name='洗衣'),
        ),
    ]
