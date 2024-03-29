# Generated by Django 2.0 on 2017-12-31 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_fullrent', models.BooleanField(default=True, verbose_name='可租狀態')),
                ('room_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='房號')),
                ('room_rent', models.PositiveIntegerField(blank=True, null=True, verbose_name='價位')),
                ('room_description', models.CharField(blank=True, max_length=50, null=True, verbose_name='其他優點')),
            ],
            options={
                'verbose_name_plural': '空屋資訊',
            },
        ),
        migrations.AlterModelOptions(
            name='suites',
            options={'verbose_name_plural': '案件資訊'},
        ),
        migrations.AddField(
            model_name='suites',
            name='suite_elecfee',
            field=models.CharField(default='5元|台電,', max_length=10, verbose_name='電費計算'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='room_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suite.Suites'),
        ),
    ]
