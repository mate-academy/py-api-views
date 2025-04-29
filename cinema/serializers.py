from rest_framework import serializers
from .models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "actors", "genres"]

    def create(self, validated_data):
        actors_data = validated_data.pop("actors")
        genres_data = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors_data)
        movie.genres.set(genres_data)
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop("actors", None)
        genres_data = validated_data.pop("genres", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if actors_data is not None:
            instance.actors.set(actors_data)
        if genres_data is not None:
            instance.genres.set(genres_data)

        return instance
