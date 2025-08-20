from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True, max_length=255)
    last_name = serializers.CharField(required=True, max_length=255)

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
    name = serializers.CharField(required=True, max_length=255)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    def validate_name(self, value):
        genres = Genre.objects.all()
        if self.instance:
            genres = genres.exclude(id=self.instance.id)
        if genres.filter(name=value).exists():
            raise serializers.ValidationError("Genre already exists")
        return value


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    rows = serializers.IntegerField(required=True, min_value=1)
    seats_in_row = serializers.IntegerField(required=True, min_value=1)

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
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    duration = serializers.IntegerField()

    def create(self, validated_data):
        actors_instance = validated_data.pop("actors")
        genres_instance = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors_instance)
        movie.genres.set(genres_instance)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.actors.set(
            validated_data.get(
                "actors",
                instance.actors.all()
            )
        )
        instance.genres.set(
            validated_data.get(
                "genres",
                instance.genres.all()
            )
        )

        instance.save()

        return instance
