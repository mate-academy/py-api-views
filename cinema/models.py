from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    actors = models.ManyToManyField(Actor, verbose_name="movies")
    genres = models.ManyToManyField(Genre, verbose_name="movies")

    def __str__(self):
        return self.title
