from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_actor_cinemahall_genre_movie_actors_movie_genres"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
