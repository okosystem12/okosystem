# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-10-07 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0016_auto_20221004_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='controluser',
            name='livePlace',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livePlace', to='Site.Place', verbose_name='Место жительства'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='birthPlace',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='birthPlace', to='Site.Place', verbose_name='Место рождения'),
        ),
    ]
