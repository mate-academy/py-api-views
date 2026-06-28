from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


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


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Actor.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Genre.objects.all())

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres",
        ]

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])

        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        movie.genres.set(genres)
        return movie

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)

        return instance
