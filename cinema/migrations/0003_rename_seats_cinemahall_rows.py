# Generated by Django 4.1 on 2024-03-15 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='seats',
            new_name='rows',
        ),
    ]
