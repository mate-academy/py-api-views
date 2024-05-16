from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    actors = models.ManyToManyField(to=Actor, related_name="actors")
    genres = models.ManyToManyField(to=Genre, related_name="genres")

    def __str__(self):
        return self.title
