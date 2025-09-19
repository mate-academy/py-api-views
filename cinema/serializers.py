from rest_framework import serializers

from .models import Actor, Genre, Movie, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    def create(self, validated_data):
        validated_data.pop("actors")
        validated_data.pop("genres")

        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        genres = validated_data.pop("genres", None)

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        if actors is not None:
            instance.actors.set(actors)

        if genres is not None:
            instance.genres.set(genres)

        instance.save()

        return instance
