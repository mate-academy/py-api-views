from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=255,
        validators=[
            UniqueValidator(queryset=Genre.objects.all())
        ]
    )

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = ActorSerializer(read_only=True, many=True)
    genres = GenreSerializer(read_only=True, many=True)

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)

        genres = self.initial_data.get("genres", None)
        if genres is not None:
            genres_instances = []
            for genre in genres:
                try:
                    genres_instances.append(Genre.objects.get(pk=genre["id"]))
                except genre.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Genre with id {genre["id"]} does not exist."
                    )
            movie.genres.set(genres_instances)

        actors = self.initial_data.get("actors", None)
        if actors is not None:
            actors_instances = []
            for actor in actors:
                try:
                    actors_instances.append(Actor.objects.get(pk=actor["id"]))
                except actor.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Actor with id {actor["id"]} does not exist."
                    )
            movie.actors.set(actors_instances)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "title", instance.title
        )
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get(
            "duration", instance.duration
        )

        genres = self.initial_data.get("genres", None)
        if genres is not None:
            genres_instances = []
            for genre in genres:
                try:
                    genres_instances.append(Genre.objects.get(pk=genre["id"]))
                except genre.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Genre with id {genre["id"]} does not exist."
                    )
            instance.genres.set(genres_instances)

        actors = self.initial_data.get("actors", None)
        if actors is not None:
            actors_instances = []
            for actor in actors:
                try:
                    actors_instances.append(Actor.objects.get(pk=actor["id"]))
                except actor.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Actor with id {actor["id"]} does not exist."
                    )
            instance.actors.set(actors_instances)

        instance.save()
        return instance
