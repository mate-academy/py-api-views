from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True)
    actors = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        movie = Movie.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            duration=validated_data["duration"]
        )

        actors = Actor.objects.filter(id__in=validated_data.get("actors", []))
        genres = Genre.objects.filter(id__in=validated_data.get("genres", []))

        movie.actors.set(actors)
        movie.genres.set(genres)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        actors = Actor.objects.filter(id__in=validated_data.get("actors", []))
        genres = Genre.objects.filter(id__in=validated_data.get("genres", []))

        instance.actors.set(actors)
        instance.genres.set(genres)

        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True, max_length=64)
    last_name = serializers.CharField(required=True, max_length=64)

    def create(self, validated_data) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Actor:
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
    name = serializers.CharField(required=True, max_length=64)

    def create(self, validated_data) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Genre:
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=64)
    rows = serializers.IntegerField(required=True, min_value=1)
    seats_in_row = serializers.IntegerField(required=True, min_value=1)

    def create(self, validated_data) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data) -> CinemaHall:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()

        return instance
