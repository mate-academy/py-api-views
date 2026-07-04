from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "genres"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "actors"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "cinema-halls"
        ordering = ["name"]

    def __str__(self):
        return ("{} (rows: {}, seats: {})".format(
            self.name,
            self.rows,
            self.seats_in_row)
        )


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="in minutes")
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
    )

    def __str__(self):
        return "{} ({} minutes)".format(self.title, self.duration)
