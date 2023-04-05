from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=60, unique=True)


class Actor(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class CinemaHall(models.Model):
    name = models.CharField(max_length=60)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(to=Actor, related_name="movies")
    genres = models.ManyToManyField(to=Genre, related_name="movies")

    def __str__(self):
        return self.title
