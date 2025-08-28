from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.rows}x{self.seats_in_row})"

    @property
    def capacity(self):
        """Total number of seats in the cinema hall"""
        return self.rows * self.seats_in_row


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()  # duration in minutes
    actors = models.ManyToManyField(Actor, related_name='actors', blank=True)
    genres = models.ManyToManyField(Genre, related_name='genres', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @property
    def duration_display(self):
        """Display duration in hours and minutes format"""
        hours = self.duration // 60
        minutes = self.duration % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"