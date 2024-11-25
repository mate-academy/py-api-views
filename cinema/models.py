from django.db import models

CHAR_FIELD_MAX_LENGTH = 255


class CinemaHall(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    last_name = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title
