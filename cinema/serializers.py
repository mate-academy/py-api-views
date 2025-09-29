from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import empty

from cinema.models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        required=False,
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        required=False,
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres",
        )

    @transaction.atomic
    def create(self, validated_data):
        # Extrai M2M antes de criar
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)

        # Persiste relações após salvar
        if actors:
            movie.actors.set(actors)
        if genres:
            movie.genres.set(genres)
        return movie

    @transaction.atomic
    def update(self, instance, validated_data):
        # Usamos 'empty' para distinguir: ausente (não mexe) vs lista vazia (limpa)
        actors = validated_data.pop("actors", empty)
        genres = validated_data.pop("genres", empty)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if actors is not empty:
            instance.actors.set(actors)  # [] limpa; [ids] substitui
        if genres is not empty:
            instance.genres.set(genres)
        return instance
