from rest_framework import serializers

from cinema.models import (
    Movie,
    CinemaHall,
    Actor,
    Genre
)


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True
    )
    duration = serializers.IntegerField()

    def create(self, validated_data):
        actors_data = validated_data.pop("actors", [])
        genres_data = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors_data)
        movie.genres.set(genres_data)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        if "actors" in validated_data:
            actors_data = validated_data.pop("actors", [])
            instance.actors.set(actors_data)
        if "genres" in validated_data:
            genres_data = validated_data.pop("genres", [])
            instance.genres.set(genres_data)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
