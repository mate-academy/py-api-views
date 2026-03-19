from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "genres"

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        verbose_name_plural = "cinema_halls"

    def __str__(self):
        return (
            f"{self.name}: "
            f"{self.rows} rows, "
            f"{self.seats_in_row} "
            f"seats in a row"
        )


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return (
            f"{self.title},"
            f"{self.duration} minutes, "
            f"Actors: {self.actors}, "
            f"Genres: {self.genres}"
        )
