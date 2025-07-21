from django.core.validators import MinValueValidator
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Actor: {self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Genre: {self.name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField(validators=[MinValueValidator(1)])
    seats_in_row = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Cinema Hall: {self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return f"Title: {self.title}, duration: {self.duration}"
