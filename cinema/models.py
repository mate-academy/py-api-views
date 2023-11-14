from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    related_name = "movies"
    actors = models.ManyToManyField(
        to=Actor,
        related_name=related_name
    )
    genres = models.ManyToManyField(
        to=Genre,
        related_name=related_name
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.title
