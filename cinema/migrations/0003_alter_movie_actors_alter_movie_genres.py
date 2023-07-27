# Generated by Django 4.1 on 2023-07-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0002_actor_cinemahall_genre_alter_movie_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(related_name="movies", to="cinema.actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(related_name="movies", to="cinema.genre"),
        ),
    ]
