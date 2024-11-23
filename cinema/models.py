from django.db import models


MAX_LENGTH = 255


class Actor(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True)

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField()
    actors = models.ManyToManyField(to=Actor, related_name="movies")
    genres = models.ManyToManyField(to=Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
