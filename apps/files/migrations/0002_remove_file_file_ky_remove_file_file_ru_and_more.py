# Generated by Django 5.0 on 2024-03-21 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_ky',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_ru',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name_ky',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name_ru',
        ),
    ]
