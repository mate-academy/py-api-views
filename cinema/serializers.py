from rest_framework import serializers

from cinema.models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row",
            instance.seats_in_row
        )
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = ActorSerializer(many=True, required=False)
    genres = GenreSerializer(many=True, required=False)

    def create(self, validated_data: dict) -> Movie:
        actors_data = validated_data.pop("actors", [])
        genres_data = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)

        if actors_data:
            for actor_data in actors_data:
                actor = Actor.objects.get(id=actor_data["id"])
                movie.actors.add(actor)

        if genres_data:
            for genre_data in genres_data:
                genre = Genre.objects.get(id=genre_data["id"])
                movie.genres.add(genre)

        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        actors_data = validated_data.pop("actors", None)
        genres_data = validated_data.pop("genres", None)

        instance.title = validated_data.get(
            "title", instance.title
        )
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get(
            "duration",
            instance.duration
        )

        if actors_data is not None:
            instance.actors.clear()
            for actor_data in actors_data:
                actor = Actor.objects.get(id=actor_data["id"])
                instance.actors.add(actor)

        if genres_data is not None:
            instance.genres.clear()
            for genre_data in genres_data:
                genre = Genre.objects.get(id=genre_data["id"])
                instance.genres.add(genre)

        instance.save()
        return instance
