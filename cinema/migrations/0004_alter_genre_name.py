# Generated by Django 4.1 on 2022-11-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
