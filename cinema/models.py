from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="genres")
    genres = models.ManyToManyField(Genre, related_name="genres")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
