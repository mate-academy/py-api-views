from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField("Actor")
    genres = models.ManyToManyField("Genre")

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return (f"First_name: {self.first_name},"
                f"Last_name: {self.last_name}")


class Genre(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        constraints = [
            UniqueConstraint(fields=
                            [ "name",], name="unique_name")]


    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return (f"cinema hall: {self.name},"
                f"rows: {self.rows},"
                f"seats: {self.seats_in_row}")
