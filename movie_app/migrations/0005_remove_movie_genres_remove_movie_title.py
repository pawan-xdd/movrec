# Generated by Django 5.0.1 on 2024-01-31 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_genre_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
    ]
