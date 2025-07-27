from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


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
        many=True, queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        genres_data = validated_data.pop("genres")
        actors_data = validated_data.pop("actors")
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres_data)
        movie.actors.set(actors_data)
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop("actors", None)
        if actors_data:
            instance.actors.set(actors_data)
        genres_data = validated_data.pop("genres", None)
        if genres_data:
            instance.genres.set(genres_data)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance
