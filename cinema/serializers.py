from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        filter = (
            "id",
            "first_name",
            "last_name",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        filter = (
            "id",
            "name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        filter = (
            "id",
            "name",
            "rows",
            "seats_in_rows",
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres",
        )
