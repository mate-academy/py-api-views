from django.core.validators import MinValueValidator
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255, null=False)
    rows = models.IntegerField(null=False, validators=[MinValueValidator(1)])
    seats_in_row = models.IntegerField(
        null=False,
        validators=[MinValueValidator(1)]
    )

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    actors = models.ManyToManyField(Actor, related_name="movies_as_actor")
    genres = models.ManyToManyField(Genre, related_name="movies_in_genre")

    def __str__(self):
        return self.title
