# Generated by Django 4.1 on 2023-04-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0002_actor_cinemahall_genre_alter_movie_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actor",
            options={"ordering": ["last_name"]},
        ),
        migrations.AlterField(
            model_name="actor",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="actor",
            name="last_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="cinemahall",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
