from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        default_related_name = "actors"


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        default_related_name = "genres"


class CinemaHall(models.Model):
    name = models.CharField(unique=True, max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        default_related_name = "cinema_halls"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    actors = models.ManyToManyField(to=Actor)
    genres = models.ManyToManyField(to=Genre)

    class Meta:
        default_related_name = "movies"

    def __str__(self):
        return self.title
