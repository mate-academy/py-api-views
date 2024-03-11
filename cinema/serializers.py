from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cinema.models import Movie, Genre, Actor, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.StringRelatedField(
        many=True, read_only=True
    )
    genres = serializers.StringRelatedField(
        many=True, read_only=True
    )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=Genre.objects.all())]
    )

    def create(self, validated_data) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Genre:
        instance.name = validated_data.get("name", instance.name)

        instance.save()

        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Actor:
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )

        instance.save()

        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    rows = serializers.IntegerField(min_value=0)
    seats_in_row = serializers.IntegerField(min_value=0)

    def create(self, validated_data) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data) -> CinemaHall:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data("seats_in_row", instance.seats_in_row)

        instance.save()

        return instance
