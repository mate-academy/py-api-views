from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=60)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies_acted_in")
    genres = models.ManyToManyField(Genre, related_name="movies_of_genre")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
