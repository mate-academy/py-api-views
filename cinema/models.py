from django.db import models
from django.db.models.functions import Lower


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField("Actor")
    genres = models.ManyToManyField("Genre")
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"), name="unique_genre_name_ci"
            )
        ]

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name

    def capacity(self):
        return self.rows * self.seats_in_row
