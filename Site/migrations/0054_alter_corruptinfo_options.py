# Generated by Django 3.2.16 on 2022-10-21 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0053_auto_20221021_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corruptinfo',
            options={'ordering': ['value', 'pk'], 'verbose_name': 'Ключевое слово', 'verbose_name_plural': 'Ключевые слова'},
        ),
    ]
