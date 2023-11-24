from rest_framework import serializers
from collections import OrderedDict

from django.shortcuts import get_list_or_404

from cinema.models import Movie, Genre, Actor, CinemaHall


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    def create(self, validated_data: OrderedDict) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self, instance: Actor, validated_data: OrderedDict) -> Actor:
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data: OrderedDict) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data: OrderedDict) -> Genre:
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data: OrderedDict) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(
            self,
            instance: CinemaHall,
            validated_data: OrderedDict
    ) -> CinemaHall:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data: OrderedDict) -> Movie:
        actors_data = validated_data.pop("actors", None)
        genres_data = validated_data.pop("genres", None)

        movie = Movie.objects.create(**validated_data)
        if actors_data:
            actors = get_list_or_404(Actor, actors_data)
            movie.actors.set(actors)

        if genres_data:
            genres = get_list_or_404(Genre, genres_data)
            movie.genres.set(genres)

        return movie

    def update(self, instance: Movie, validated_data: OrderedDict) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        actors_data = validated_data.get("actors")
        genres_data = validated_data.get("genres")

        if actors_data:
            actors = get_list_or_404(Actor, actors_data)
            instance.actors.set(actors)

        if genres_data:
            genres = get_list_or_404(Genre, genres_data)
            instance.genres.set(genres)

        instance.save()
        return instance
