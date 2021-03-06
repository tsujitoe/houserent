# Generated by Django 2.0 on 2018-01-01 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0003_auto_20171231_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='House_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_subject', models.CharField(max_length=100)),
                ('p_date', models.DateTimeField(auto_now=True)),
                ('p_image', models.ImageField(upload_to='suite_photos')),
                ('P_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo', to='suite.Suites')),
            ],
            options={
                'verbose_name_plural': '案件照片',
            },
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_description',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='其他優點'),
        ),
    ]
