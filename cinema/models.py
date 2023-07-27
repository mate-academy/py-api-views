from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=31)
    rows = models.PositiveSmallIntegerField()
    seats_in_row = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique seat in the hall",
                fields=[
                    "name", "rows", "seats_in_row"
                ]
            )
        ]

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(
        to=Actor,
        related_name="movies"
    )
    genres = models.ManyToManyField(
        to=Genre,
        related_name="movies"
    )

    def __str__(self) -> str:
        return self.title
