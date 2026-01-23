from django.db import models # Importação do módulo models

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True) # Requisito: unique=True

    def __str__(self):
        return self.name

class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField() # Duração em minutos, por exemplo
    actors = models.ManyToManyField(Actor, related_name="movies") # Requisito: related_name
    genres = models.ManyToManyField(Genre, related_name="movies") # Requisito: related_name

    def __str__(self):
        return self.title
