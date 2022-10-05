# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-10-04 13:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0015_remove_universities_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='controluser',
            name='birthPlace',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.Place', verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
