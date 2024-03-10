from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
