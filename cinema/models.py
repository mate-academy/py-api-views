from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    actors = models.ManyToManyField(Actor, verbose_name="movies")
    genres = models.ManyToManyField(Genre, verbose_name="movies")

    def __str__(self):
        return self.title
