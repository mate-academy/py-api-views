from rest_framework import serializers
from cinema.models import Actor, CinemaHall, Genre, Movie


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
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Genre.objects.all(),
        required=False
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Actor.objects.all(),
        required=False
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")
