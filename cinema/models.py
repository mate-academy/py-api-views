from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.SmallIntegerField()
    actors = models.ManyToManyField("Actor", related_name="actors")
    genres = models.ManyToManyField("Genre", related_name="genre")

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.SmallIntegerField()
    seats_in_row = models.SmallIntegerField()

    def __str__(self):
        return self.name
