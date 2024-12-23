from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
