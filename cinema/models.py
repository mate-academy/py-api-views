from django.db import models


class Actor(models.Model):
    first_name = models.fields.CharField(max_length=100)
    last_name = models.fields.CharField(max_length=100)


class Genre(models.Model):
    name = models.fields.CharField(max_length=100, unique=True)


class CinemaHall(models.Model):
    name = models.fields.CharField(max_length=100)
    rows = models.fields.IntegerField(default=0)
    seats_in_row = models.fields.IntegerField(default=0)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
