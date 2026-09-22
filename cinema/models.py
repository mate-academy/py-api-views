"""Database models for the cinema application."""

from __future__ import annotations

from django.db import models


class Genre(models.Model):
    """A category assigned to movies."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        """Return the genre name."""
        return self.name


class Actor(models.Model):
    """A performer who can be associated with movies."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Return the actor's full name."""
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    """A physical hall in which films can be shown."""

    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        """Return the cinema hall name."""
        return self.name


class Movie(models.Model):
    """A film, including its cast and genres."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)

    def __str__(self) -> str:
        """Return the movie title."""
        return self.title
