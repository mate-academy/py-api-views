from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.PositiveSmallIntegerField()
    seats_in_row = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "cinema_hall"
        verbose_name_plural = "cinema_halls"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
