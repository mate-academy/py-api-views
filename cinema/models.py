from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    class Meta:
        ordering = ["first_name"]

    def __str__(self) -> str:
        return f"Full name: {self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=70, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=70)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"Name: {self.name}" \
               f" (rows: {self.rows} seats: {self.seats_in_row}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(to=Actor)
    genres = models.ManyToManyField(to=Genre)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
