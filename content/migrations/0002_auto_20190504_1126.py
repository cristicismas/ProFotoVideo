# Generated by Django 2.2 on 2019-05-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='date',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='date',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]
