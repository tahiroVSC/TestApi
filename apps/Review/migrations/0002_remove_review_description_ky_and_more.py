# Generated by Django 5.0 on 2024-03-21 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='description_ky',
        ),
        migrations.RemoveField(
            model_name='review',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='review',
            name='jobtitle_ky',
        ),
        migrations.RemoveField(
            model_name='review',
            name='jobtitle_ru',
        ),
        migrations.RemoveField(
            model_name='review',
            name='name_ky',
        ),
        migrations.RemoveField(
            model_name='review',
            name='name_ru',
        ),
    ]