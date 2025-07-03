
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.start_time.strftime('%Y-%m-%d %H:%M')} in {self.cinema_hall.name}"