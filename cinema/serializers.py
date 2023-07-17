from rest_framework import serializers

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall
)


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
        required=False,
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Movie
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializers(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"
