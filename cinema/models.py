from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(
        "Actor",
        related_name="movies",
        blank=True,
    )
    genres = models.ManyToManyField(
        "Genre",
        related_name="movies",
        blank=True,
    )

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=128)
    rows = models.IntegerField(default=0)
    seats_in_row = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
