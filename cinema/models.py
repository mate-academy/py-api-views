from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name, self.last_name


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(40), MinValueValidator(0), ]
    )
    seats_in_row = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(50), MinValueValidator(0), ]
    )

    def __str__(self):
        return self.name, self.rows, self.seats_in_row


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
