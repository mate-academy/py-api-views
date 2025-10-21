# cinema/serializers.py
from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True, required=False
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=False
    )

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)
        movie = Movie.objects.create(**validated_data)
        if actors is not None:
            movie.actors.set(actors)
        if genres is not None:
            movie.genres.set(genres)
        movie.save()
        return movie

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)
        return instance
