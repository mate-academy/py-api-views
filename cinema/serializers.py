from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "actors",
            "genres",
            "duration",
        ]
