from rest_framework import serializers

from cinema.models import Movie, Actor, CinemaHall, Genre


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True
    )
    duration = serializers.IntegerField()

    def create(self, validated_data):
        actors_data = validated_data.pop("actors", [])
        genres_data = validated_data.pop("genres", [])

        movie = Movie.objects.create(**validated_data)

        for actor_data in actors_data:
            actor, created = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)

        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()
        for field_name in ["actors", "genres"]:
            if field_name in validated_data:
                field = getattr(instance, field_name)
                field.set(validated_data[field_name])

        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)

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
    name = serializers.CharField(max_length=64)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=64)
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
