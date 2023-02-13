from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=55, unique=True)


class Actor(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)


class CinemaHall(models.Model):
    name = models.CharField(max_length=55)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(to=Genre, related_name="movies")
    actors = models.ManyToManyField(to=Actor, related_name="movies")

    def __str__(self):
        return self.title
