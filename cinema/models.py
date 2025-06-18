from django.db import models
from datetime import date


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(default=90)
    release_date = models.DateField(default=date.today)
    rating = models.FloatField(default=0.0)
    actors = models.ManyToManyField("Actor", related_name="movies")
    genres = models.ManyToManyField("Genre", related_name="movies")

    def __str__(self):
        return self.title
