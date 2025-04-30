from django.db import transaction
from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


class GenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class ActorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
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
    genres = GenreSerializer(many=True, required=False)
    actors = ActorSerializer(many=True, required=False)

    def create(self, validated_data):
        with (transaction.atomic()):
            genres_data = validated_data.pop("genres", [])
            actors_data = validated_data.pop("actors", [])
            movie = Movie.objects.create(**validated_data)

            for genre_data in genres_data:
                genre = Genre.objects.create(**genre_data)
                movie.genres.add(genre)
            for actor_data in actors_data:
                actor = Actor.objects.create(**actor_data)
                movie.actors.add(actor)

            movie.save()
            return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get(
            "duration", instance.duration
        )
        genres = validated_data.get("genres", [])
        if genres:
            instance.genres.set(genres)
        actors = validated_data.get("actors", [])
        if actors:
            instance.actors.set(actors)
        instance.save()
        return instance
