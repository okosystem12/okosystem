# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-10-31 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0070_auto_20221031_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='firstName',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='lastName',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='value',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='value',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='social',
            name='value',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='vch',
            name='number',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Номер ВЧ'),
        ),
    ]
