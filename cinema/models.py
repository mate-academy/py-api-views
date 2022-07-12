from django.db import models


class Actor(models.Model):
    """Actor model"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name_plural = "Actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    """Genre model"""

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Genres"

    def __str__(self):
        return f"{self.name}"


class CinemaHall(models.Model):
    """Cinema hall model"""

    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Cinema_Halls"

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    """Movie model"""

    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title}"
