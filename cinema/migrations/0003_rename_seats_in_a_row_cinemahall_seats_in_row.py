# Generated by Django 4.1 on 2024-01-19 09:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0002_actor_cinemahall_genre_movie_actors_movie_genres"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cinemahall",
            old_name="seats_in_a_row",
            new_name="seats_in_row",
        ),
    ]
