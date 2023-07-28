# Generated by Django 4.1 on 2023-07-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "cinema",
            "0003_remove_movie_actors_remove_movie_genres_movie_actors_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="cinema.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="cinema.genre"
            ),
        ),
    ]
