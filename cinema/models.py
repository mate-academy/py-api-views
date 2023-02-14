from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    actors = models.ManyToManyField(to=Actor)
    genres = models.ManyToManyField(to=Genre)
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title
