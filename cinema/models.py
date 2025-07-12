from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return f"Actor name: {self.first_name} {self.last_name}"


    class Meta:
        verbose_name_plural = "actors"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Genre: {self.name}"

    class Meta:
        verbose_name_plural = "genres"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"Cinema hall name: {self.name}, rows: {self.rows}, seats: {self.seats_in_row}"

    class Meta:
        verbose_name_plural = "cinema halls"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return f"Title: {self.title}, duration: {self.duration}"

    class Meta:
        verbose_name_plural = "movies"
