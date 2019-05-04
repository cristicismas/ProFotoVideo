# Generated by Django 2.2 on 2019-05-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slides', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('thumbnail', models.URLField(blank=True)),
                ('title', models.CharField(blank=True, max_length=70)),
                ('date', models.DateField(blank=True, null=True)),
                ('isFeatured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=70)),
                ('date', models.DateField(blank=True, null=True)),
                ('isFeatured', models.BooleanField(default=False)),
            ],
        ),
    ]