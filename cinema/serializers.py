from rest_framework import serializers

from cinema.models import Movie, Actor, CinemaHall, Genre


class ActorSerializer(serializers.Serializer):
    """Serializer for Actor model"""

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)

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


class GenreSerializer(serializers.Serializer):
    """Serializer for Genre model"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    """Serializer for CinemaHall model"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    rows = serializers.IntegerField(required=True)
    seats_in_row = serializers.IntegerField(required=True)

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
    """Serializer for Movie model"""

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    # actors = ActorSerializer(many=True, required=True)
    # genres = GenreSerializer(many=True, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        # instance.actors = validated_data.get("actors", instance.actors)
        # instance.genres = validated_data.get("genres", instance.genres)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
