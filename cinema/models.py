from django.db import models


class Actor(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["last_name", ]
        verbose_name_plural = "Actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name", ]
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return f"{self.name}, rows: {self.rows}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    duration = models.PositiveIntegerField()

    class Meta:
        ordering = ["title", ]
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
