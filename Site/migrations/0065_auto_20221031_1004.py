# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-10-31 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0064_column_searchable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusersvk',
            name='id_user',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='id пользователя'),
        ),
    ]
