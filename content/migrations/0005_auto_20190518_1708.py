# Generated by Django 2.2.1 on 2019-05-18 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20190518_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-updated']},
        ),
    ]