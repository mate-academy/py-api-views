from rest_framework import serializers

from cinema.models import Movie, CinemaHall, Actor, Genre


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
        queryset=Actor.objects.all(),
        many=True)
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])

        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        movie.genres.set(genres)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description",
            instance.description)
        instance.duration = validated_data.get("duration", instance.duration)

        if "actors" in validated_data:
            instance.actors.set(validated_data["actors"])

        if "genres" in validated_data:
            instance.genres.set(validated_data["genres"])

        instance.save()
        return instance
