from rest_framework import serializers

# Убедись, что вместо 'cinema' стоит правильное название твоего приложения,
# если оно отличается.
from cinema.models import Genre, Actor, CinemaHall, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all(), required=False)
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=False)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "actors", "genres")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["actors"] = ActorSerializer(
            instance.actors.all(), many=True).data
        representation["genres"] = GenreSerializer(
            instance.genres.all(), many=True).data
        return representation


class MovieListSerializer(MovieSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True, required=False, read_only=True)
    genres = serializers.PrimaryKeyRelatedField(
        many=True, required=False, read_only=True)
