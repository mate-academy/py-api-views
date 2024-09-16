from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="actors")
    genres = models.ManyToManyField(Genre, related_name="genres")

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=55)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name
