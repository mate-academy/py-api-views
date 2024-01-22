from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)


class Genre(models.Model):
    name = models.CharField(max_length=10, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=10)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, default=None, null=True)
    genres = models.ManyToManyField(Genre, null=True, default=None)

    def __str__(self):
        return self.title
