from rest_framework.serializers import ModelSerializer
from cinema.models import Movie, Actor, Genre, CinemaHall


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "actors", "genres", "duration"]
