from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "genres"

    def __str__(self):
        return f"{self.name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "cinema_halls"

    def __str__(self):
        num_seats = self.rows * self.seats_in_row
        return f"Cinema Hall:{self.name}. Amount of seats: {num_seats}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies_of_actor")
    genres = models.ManyToManyField(Genre, related_name="movies_with_genre")
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
