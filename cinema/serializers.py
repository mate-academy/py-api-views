from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cinema.models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row"]


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    print(actors)
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    def create(self, validated_data):
        actors = validated_data.pop("actors")
        genres = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        movie.genres.set(genres)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        if "actors" in validated_data:
            actors = validated_data.pop("actors")
            instance.actors.set(actors)

        if "genres" in validated_data:
            genres = validated_data.pop("genres")
            instance.genres.set(genres)

        instance.save()

        return instance
