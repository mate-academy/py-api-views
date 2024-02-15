from rest_framework import serializers
from cinema.models import Movie, CinemaHall, Genre, Actor


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True)
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.actors.set(
            validated_data.get("actors", instance.actors.all()))
        instance.genres.set(
            validated_data.get("genres", instance.genres.all()))

        instance.save()
        return instance


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
