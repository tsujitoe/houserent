# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180228_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeinfo',
            name='home_equipment',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('桌子', '桌子'), ('椅子', '椅子'), ('衣櫃', '衣櫃'), ('床', '床'), ('沙發', '沙發'), ('熱水器', '熱水器'), ('電視', '電視'), ('冰箱', '冰箱'), ('冷氣', '冷氣'), ('洗衣機', '洗衣機')], max_length=100, null=True, verbose_name='設備包含'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_garbage',
            field=models.CharField(blank=True, choices=[('社區集中', '社區集中'), ('子母車', '子母車'), ('自理', '自理'), ('其他補充', '其他補充')], max_length=20, null=True, verbose_name='垃圾處理'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_how_inter_door',
            field=models.CharField(blank=True, choices=[('公司Key', '公司Key'), ('屋主開門', '屋主開門'), ('管理室', '管理室'), ('密碼', '密碼'), ('其他補充', '其他補充')], max_length=50, null=True, verbose_name='如何進入房門'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_how_manage',
            field=models.CharField(blank=True, choices=[('物管公司', '物管公司'), ('管理員', '管理員'), ('無', '無'), ('其他補充', '其他補充')], max_length=20, null=True, verbose_name='管理方式'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_include',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('水', '水'), ('網路', '網路'), ('第四台', '第四台'), ('垃圾費', '垃圾費'), ('管理費', '管理費'), ('其他', '其他')], max_length=100, null=True, verbose_name='包含雜費'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_park',
            field=models.CharField(default='平面 | 機上/下，車號：', max_length=50, verbose_name='車位'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_people_limit',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('學生', '學生'), ('上班族', '上班族'), ('家庭', '家庭'), ('禁男', '禁男'), ('禁女', '禁女'), ('禁小孩', '禁小孩'), ('禁40以上', '禁40以上'), ('禁拜拜', '禁拜拜'), ('禁煮飯', '禁煮飯'), ('其他補充', '其他補充')], max_length=100, null=True, verbose_name='身份限制'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_pet_limit',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('全部禁寵', '全部禁寵'), ('可寵', '可寵'), ('可貓', '可貓'), ('可狗', '可狗'), ('其他補充', '其他補充')], max_length=100, null=True, verbose_name='寵物限制'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_rent',
            field=models.CharField(blank=True, default='5000', max_length=20, null=True, verbose_name='租金'),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='home_type',
            field=models.CharField(blank=True, choices=[('大樓', '大樓'), ('公寓', '公寓'), ('透天', '透天'), ('其他', '其他')], max_length=20, null=True, verbose_name='型態'),
        ),
        migrations.AlterField(
            model_name='homemediainfo',
            name='home_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title_photo', to='home.HomeInfo'),
        ),
        migrations.AlterField(
            model_name='homemediainfo',
            name='home_title',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='標題'),
        ),
    ]