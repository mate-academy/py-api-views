from rest_framework import serializers

from cinema import models
from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Actor.objects.all(),
        required=False)
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Genre.objects.all(),
        required=False)

    def create(self, validated_data):

        movie = Movie.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            duration=validated_data["duration"],)
        if "actors" in validated_data:
            movie.actors.set(validated_data["actors"])
        if "genres" in validated_data:
            movie.genres.set(validated_data["genres"])
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        if "actors" in validated_data:
            instance.actors.set(validated_data["actors"])

        if "genres" in validated_data:
            instance.genres.set(validated_data["genres"])

        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name",
                                                instance.last_name)
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        movie = CinemaHall.objects.create(
            name=validated_data["name"],
            rows=validated_data["rows"],
            seats_in_row=validated_data["seats_in_row"], )
        return movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get("seats_in_row",
                                                   instance.seats_in_row)
        instance.save()
        return instance
