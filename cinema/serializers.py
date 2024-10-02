from rest_framework import serializers

from cinema.models import Movie, Genre, CinemaHall, Actor


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_genres(self, movie: Movie) -> list[str]:
        return [genre.name for genre in movie.genres.all()]

    def get_actors(self, movie: Movie) -> list[str]:
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in movie.actors.all()
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"
