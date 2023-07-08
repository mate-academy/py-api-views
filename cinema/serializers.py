from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "movies"]


class GenreSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Genre
        fields = ["id", "name", "movies"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "actors", "genres"]
