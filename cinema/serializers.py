from rest_framework import serializers
from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "actors", "genres"]

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        movie.genres.set(genres)
        return movie

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)

        instance.save()
        return instance
