from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return self.first_name + " " + self.last_name


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
