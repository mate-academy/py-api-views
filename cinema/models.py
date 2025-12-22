from django.contrib.admin.actions import delete_selected
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "actors"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Genre name: {self.name}"

    class Meta:
        ordering = ["name"]


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"CinemaHall name: {self.name}({self.rows}/{self.seats_in_row})"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",

    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"Movie title: {self.title}"
