from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    related_name = "movies"
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name=related_name)
    genres = models.ManyToManyField(Genre, related_name=related_name)

    def __str__(self):
        return str(self.title)
