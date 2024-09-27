from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'actor: "{self.first_name} {self.last_name}"'


class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f'genre: "{self.name}"'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300),
        ]
    )
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return (
            f'movie: "{self.title}"\nduration: "{self.duration}"'
        )


class CinemaHall(models.Model):
    name = models.CharField(max_length=150)
    rows = models.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(30),
        ]
    )
    seats_in_row = models.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(30),
        ]
    )

    def __str__(self):
        return (
            f'cinema hall: "{self.name}"\n'
            f'rows: "{self.rows}"'
            f'seats_in_row: "{self.seats_in_row}"'
        )
