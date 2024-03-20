from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", ]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", ]


class CinemaHallSerializer(serializers.ModelSerializer):
    rows = serializers.IntegerField(max_value=40, min_value=0, )
    seats_in_row = serializers.IntegerField(max_value=50, min_value=0, )

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", ]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id", "title", "description", "actors", "genres", "duration",
        ]
