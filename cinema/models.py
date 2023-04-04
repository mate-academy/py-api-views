from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    seats_in_row = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.name} {self.rows} {self.seats_in_row}"


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    duration = models.IntegerField(validators=[MaxValueValidator(999)])

    class Meta:
        default_related_name = "movies"

    def __str__(self):
        return f"{self.title} {self.description} {self.duration}"
