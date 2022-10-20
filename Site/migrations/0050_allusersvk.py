# Generated by Django 3.2.16 on 2022-10-20 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0049_alter_social_prefix'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllUsersVK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, default='', verbose_name='Имя')),
                ('last_name', models.TextField(blank=True, default='', verbose_name='Фамилия')),
                ('bdate', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата рождения')),
                ('home_town', models.TextField(blank=True, default='', verbose_name='Место рождения')),
                ('city', models.TextField(blank=True, default='', verbose_name='Место жительства')),
                ('id_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.social')),
            ],
            options={
                'verbose_name': 'Пользователь VK',
                'verbose_name_plural': 'Пользователи VK',
            },
        ),
    ]
