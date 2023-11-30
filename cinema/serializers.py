from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


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
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
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
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    duration = serializers.IntegerField()

    def create(self, validated_data):
        actors_data = validated_data.pop("actors")
        genres_data = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)
        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.gernes.add(genre)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        actors_data = validated_data.pop("actors")
        genres_data = validated_data.pop("genres")
        instance.actors.clear()
        instance.genres.clear()
        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            instance.actors.add(actor)
        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            instance.genres.add(genre)

        instance.save()

        return instance
