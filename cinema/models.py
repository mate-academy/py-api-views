from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)


class Genre(models.Model):
    name = models.CharField(max_length=65, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=65)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self) -> str:
        return self.title
