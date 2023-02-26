from rest_framework import serializers

from cinema.models import Movie, Actor, CinemaHall, Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
