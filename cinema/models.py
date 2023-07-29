from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(to="Actor", related_name="movies")
    genres = models.ManyToManyField(to="Genre", related_name="movies")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    class Meta:
        ordering = ["name"]

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self):
        return f"Hall name: {self.name}"
