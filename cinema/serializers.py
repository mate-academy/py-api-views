from rest_framework.serializers import ModelSerializer
from cinema.models import Movie, Genre, Actor, CinemaHall


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"
