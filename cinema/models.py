from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        ordering = ("last_name",)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.rows} rows x {self.seats_in_row} seats"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
