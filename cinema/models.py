from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "actor"
        verbose_name_plural = "actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self):
        return f"{self.name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ["name"]
        verbose_name = "cinema hall"
        verbose_name_plural = "cinema halls"

    def __str__(self):
        return f"{self.name} ({self.rows} rows x {self.seats_in_row} seats)"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
