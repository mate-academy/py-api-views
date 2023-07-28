from django.core.validators import MinValueValidator
from django.db import models


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
    rows = models.IntegerField(
        MinValueValidator(1)
    )
    seats_in_row = models.IntegerField(
        MinValueValidator(1)
    )

    def num_seats(self):
        return self.seats_in_row * self.row1

    def __str__(self):
        return f"{self.name}, {self.num_seats()}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
