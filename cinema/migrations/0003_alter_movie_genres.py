# Generated by Django 4.1 on 2022-11-16 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.genre'),
        ),
    ]
