"""Cinema database models."""
from __future__ import annotations

from django.db import models


class Genre(models.Model):
    """A unique film category."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    """A movie performer."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    """A screening room."""

    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    """A film with its cast and genres."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)

    def __str__(self) -> str:
        return self.title
