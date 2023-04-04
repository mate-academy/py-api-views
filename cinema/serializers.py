from rest_framework import serializers

from cinema.models import Movie, Genre, CinemaHall, Actor


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def get_actors(self, obj: Movie) -> list:
        return [ActorSerializer(actor).data for actor in obj.actors.all()]

    def get_genres(self, obj: Movie) -> list:
        return [GenreSerializer(genre).data for genre in obj.genres.all()]
