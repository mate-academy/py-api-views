from rest_framework import serializers
from .models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.ModelSerializer):
    # Для ManyToMany полів використовуємо PrimaryKeyRelatedField
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        required=False  # Дозволяємо пустий список
    )

    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        required=False  # Дозволяємо пустий список
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors", "genres", "duration")
