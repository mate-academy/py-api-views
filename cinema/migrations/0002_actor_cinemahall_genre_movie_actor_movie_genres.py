# Generated by Django 4.0.4 on 2022-11-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="CinemaHall",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("rows", models.SmallIntegerField()),
                ("seats_in_row", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="actor",
            field=models.ManyToManyField(to="cinema.actor"),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="cinema.genre"),
        ),
    ]
