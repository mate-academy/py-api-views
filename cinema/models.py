from django.db import models


class Actor(models.Model):
    first_name: str = models.CharField(max_length=255)
    last_name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name: str = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name: str = models.CharField(max_length=255)
    rows: int = models.IntegerField()
    seats_in_row: int = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title: str = models.CharField(max_length=255)
    description: str = models.TextField()
    duration: int = models.IntegerField()
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
    )

    def __str__(self) -> str:
        return self.title
