# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-08-22 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_auto_20220822_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controluser',
            name='birthDate',
        ),
        migrations.AddField(
            model_name='controluser',
            name='birthDay',
            field=models.IntegerField(default=0, verbose_name='День рождения'),
        ),
        migrations.AddField(
            model_name='controluser',
            name='birthMonth',
            field=models.IntegerField(default=0, verbose_name='Месяц рождения'),
        ),
        migrations.AddField(
            model_name='controluser',
            name='birthYear',
            field=models.IntegerField(default=0, verbose_name='Год рождения'),
        ),
    ]
