from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    class Meta:
        verbose_name_plural = "Actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cinema Halls"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    class Meta:
        verbose_name_plural = "Movies"
        ordering = ["title"]

    def __str__(self):
        return self.title
