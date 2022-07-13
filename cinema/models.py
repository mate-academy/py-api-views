from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return f"{self.name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField("Actor", related_name="actors")
    genres = models.ManyToManyField("Genre", related_name="genres")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title"]
