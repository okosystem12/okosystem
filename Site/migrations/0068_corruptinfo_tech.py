# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-10-31 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0067_auto_20221031_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='corruptinfo',
            name='tech',
            field=models.BooleanField(default=False, verbose_name='Управление администратором'),
        ),
    ]
