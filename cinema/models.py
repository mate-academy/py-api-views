from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)

    class Meta:
        ordering = ("last_name",)

    def __str__(self):
        return f"actor: {self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=65)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"Cinema hall: {self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"{self.title} (genre: {self.genres})"
