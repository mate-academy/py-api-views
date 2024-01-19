from django.db import models


class Actor(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name="movie_genres")
    actors = models.ManyToManyField(Actor, related_name="movie_actors")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
