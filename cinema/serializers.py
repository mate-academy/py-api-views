from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        instance.save()
        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    duration = serializers.IntegerField(min_value=1)

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


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField(min_value=1)
    seats_in_row = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
