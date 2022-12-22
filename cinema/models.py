from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=200)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="actor")
    genres = models.ManyToManyField(Genre, related_name="genre")

    def __str__(self):
        return self.title
