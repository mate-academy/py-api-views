from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return (f"{self.name}, "
                f"Rows: {self.rows}, "
                f"Sets in row: {self.seats_in_row}")


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return (f"{self.title}. "
                f"Description: {self.description}. "
                f"Duration: {self.duration}."
                f"Actors: {self.actors.all()}"
                f"Genres: {self.genres.all()}")
