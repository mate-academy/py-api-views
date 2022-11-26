from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name"]


class Genre(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class CinemaHall(models.Model):
    name = models.CharField(max_length=55, unique=True)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
