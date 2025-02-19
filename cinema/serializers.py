from rest_framework import serializers
from cinema.models import Movie, Genre, Actor, CinemaHall


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True, required=False
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=False
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "actors", "genres"]

    def create(self, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)
        instance = Movie.objects.create(**validated_data)
        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)
        return instance

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)
        instance = super().update(instance, validated_data)

        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)
        return instance


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]
