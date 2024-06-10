from rest_framework import serializers

from cinema.models import Actor
from cinema.models import CinemaHall
from cinema.models import Genre
from cinema.models import Movie


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True
    )
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres",
            "cinema_hall",
        ]

    def create(self, validated_data: dict) -> Movie:
        actors = validated_data.pop("actors")
        genres = validated_data.pop("genres")
        cinema_hall = validated_data.pop("cinema_hall")
        movie = Movie.objects.create(
            **validated_data, cinema_hall=cinema_hall
        )

        movie.actors.set(actors)
        movie.genres.set(genres)
        movie.save()

        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)
        cinema_hall = validated_data.pop("cinema_hall", None)

        for atte, value in validated_data.items():
            setattr(instance, atte, value)

        if actors:
            instance.actors.set(actors)
        if genres:
            instance.genres.set(genres)
        if cinema_hall:
            instance.cinema_hall = cinema_hall

        instance.save()

        return instance
