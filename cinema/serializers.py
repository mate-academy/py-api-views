from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.ModelSerializer):
    # Додаємо required=False, щоб дозволити створення/оновлення фільмів без обов'язкової передачі акторів та жанрів
    actors = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Actor.objects.all(), required=False)
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Genre.objects.all(), required=False)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors", "genres", "duration")
