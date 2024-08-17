from rest_framework import serializers

from cinema.models import Movie, Actor, CinemaHall, Genre


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Actor.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Genre.objects.all())

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

        instance.title = validated_data.get("title", instance.title)
        instance.description = (validated_data.get
                                ("description", instance.description))
        instance.duration = validated_data.get("duration", instance.duration)

        if actors is not None:
            instance.actors.set(actors)
        if genres is not None:
            instance.genres.set(genres)

        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    def validate_name(self, value):
        if Genre.objects.filter(name=value).exists():
            raise (serializers.ValidationError
                   ("Genre with this name already exists."))
        return value


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = (validated_data.get
                               ("first_name", instance.first_name))
        instance.last_name = (validated_data.get
                              ("last_name", instance.last_name))
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
        instance.seats_in_row = (validated_data.get
                                 ("seats_in_row", instance.seats_in_row))
        instance.save()
        return instance
