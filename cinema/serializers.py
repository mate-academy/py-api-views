# flake8: noqa: E501

from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        movie = Movie.objects.create(**validated_data)
        self.set_genres_and_actors(movie)
        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()

        self.set_genres_and_actors(instance)
        return instance

    def set_genres_and_actors(self, movie: Movie) -> None:
        genres_data = self.context["request"].data.get("genres", [])
        actors_data = self.context["request"].data.get("actors", [])

        movie.genres.set(genres_data)
        movie.actors.set(actors_data)

    def get_genres(self, movie: Movie) -> list:
        return [genre.id for genre in movie.genres.all()]

    def get_actors(self, movie: Movie) -> list:
        return [actor.id for actor in movie.actors.all()]


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data: dict) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Actor:
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def validate_name(self, name: str) -> str:
        if name and Genre.objects.filter(name=name).exists():
            raise serializers.ValidationError("Genre with this name already exists")
        return name

    def create(self, validated_data: dict) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data: dict) -> Genre:
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data: dict) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance: CinemaHall, validated_data: dict) -> CinemaHall:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()
        return instance
