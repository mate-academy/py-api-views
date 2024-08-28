from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall,
)


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "actors", "genres", "duration"]

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])

        movie = Movie.objects.create(**validated_data)

        movie.actors.set(actors)
        movie.genres.set(genres)

        return movie

    def update(self, instance, validated_data):
        # Extract the actors and genres from validated_data
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)

        # Update the Movie instance with other fields
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)

        # Save the instance
        instance.save()

        # Update the many-to-many relationships
        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)

        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
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


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row",
            instance.seats_in_row
        )
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
