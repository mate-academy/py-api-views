# Generated by Django 4.1 on 2023-08-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='cinema.genre'),
        ),
    ]
