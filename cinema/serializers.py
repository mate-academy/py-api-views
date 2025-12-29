from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])
        instance = super().create(validated_data)
        instance.actors.set(actors)
        instance.genres.set(genres)

        return instance

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])
        instance = super().update(instance, validated_data)
        instance.actors.set(actors)
        instance.genres.set(genres)

        if "actors" in validated_data:
            instance.actors.set(validated_data.get("actors"))

        if "genres" in validated_data:
            instance.genres.set(validated_data.get("genres"))

        return instance


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
