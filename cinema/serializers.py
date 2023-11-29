from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), required=False, many=True,
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), required=False, many=True,
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
        actors_data = validated_data.pop("actors", [])
        genres_data = validated_data.pop("genres", [])
        instance.actors.set(actors_data)
        instance.genres.set(genres_data)
        instance.save()

        return instance


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
