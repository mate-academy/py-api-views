from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(read_only=True, many=True)
    genres = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = "__all__"
