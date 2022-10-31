# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-10-31 14:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0071_auto_20221031_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='country',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Countries', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Regions', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='column',
            name='render',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Render', verbose_name='Рендер'),
        ),
        migrations.AlterField(
            model_name='column',
            name='table',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Table', verbose_name='Таблица'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='birthPlace',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='birthPlace', to='Site.Place', verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='livePlace',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livePlace', to='Site.Place', verbose_name='Место жительства'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='controluser',
            name='vch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Vch', verbose_name='Место военной службы'),
        ),
        migrations.AlterField(
            model_name='controluserimg',
            name='controlUser',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.ControlUser'),
        ),
        migrations.AlterField(
            model_name='controluserimg',
            name='file',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.File'),
        ),
        migrations.AlterField(
            model_name='controluserplace',
            name='controlUser',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.ControlUser'),
        ),
        migrations.AlterField(
            model_name='controluserplace',
            name='place',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Place', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='groupschecks',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='groupscorrupt',
            name='corrupt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.CorruptInfo'),
        ),
        migrations.AlterField(
            model_name='groupscorrupt',
            name='groups',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Groups'),
        ),
        migrations.AlterField(
            model_name='inf',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='infcorrupt',
            name='corrupt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.CorruptInfo'),
        ),
        migrations.AlterField(
            model_name='infcorrupt',
            name='inf',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Inf'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='controlUser',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.ControlUser'),
        ),
        migrations.AlterField(
            model_name='patterncolumn',
            name='column',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Column', verbose_name='Столбец'),
        ),
        migrations.AlterField(
            model_name='patterncolumn',
            name='pattern',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.PatternTable', verbose_name='Шаблон'),
        ),
        migrations.AlterField(
            model_name='patterntable',
            name='table',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Table', verbose_name='Таблица'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='controlUser',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.ControlUser'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='photoschecks',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='photoscorrupt',
            name='corrupt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.CorruptInfo'),
        ),
        migrations.AlterField(
            model_name='photoscorrupt',
            name='photo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Photos'),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Cities', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Countries', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='place',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Regions', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='post',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='postcorrupt',
            name='corrupt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.CorruptInfo'),
        ),
        migrations.AlterField(
            model_name='postcorrupt',
            name='post',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Post'),
        ),
        migrations.AlterField(
            model_name='postschecks',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='country',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Countries', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='social',
            name='controlUser',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.ControlUser'),
        ),
        migrations.AlterField(
            model_name='status',
            name='stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.StatusStage', verbose_name='Этап'),
        ),
        migrations.AlterField(
            model_name='video',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='videochecks',
            name='social',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Social'),
        ),
        migrations.AlterField(
            model_name='videocorrupt',
            name='corrupt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.CorruptInfo'),
        ),
        migrations.AlterField(
            model_name='videocorrupt',
            name='video',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.Video'),
        ),
    ]
