# Generated by Django 4.1 on 2023-04-16 17:32

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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
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
                ("name", models.CharField(max_length=50)),
                ("rows", models.PositiveIntegerField()),
                ("seats_in_row", models.PositiveIntegerField()),
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name="movie",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(to="cinema.actor"),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="cinema.genre"),
        ),
    ]
