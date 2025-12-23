from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField
)

from .models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(ModelSerializer):
    actors = PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        required=False
    )
    genres = PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        required=False
    )

    class Meta:
        model = Movie
        fields = "__all__"
