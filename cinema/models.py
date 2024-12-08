from django.db import models
from rest_framework.validators import UniqueTogetherValidator


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField("Actor", related_name="movies")
    genres = models.ManyToManyField("Genre", related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        pass


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.SmallIntegerField()
    seats_in_row = models.SmallIntegerField()

    def __str__(self):
        return self.name
