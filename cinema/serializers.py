from rest_framework import serializers
from cinema.models import Movie, Actor, Genre, CinemaHall, Screening


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
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
        instance.seats_in_row = validated_data.get("seats_in_row", instance.seats_in_row)
        instance.save()
        return instance


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        actors = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        movie.actors.set(actors)
        return movie

    def update(self, instance, validated_data):
        genres = validated_data.pop('genres', None)
        actors = validated_data.pop('actors', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)

        return instance

class ScreeningSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(queryset=CinemaHall.objects.all())

    class Meta:
        model = Screening
        fields = ['id', 'movie', 'cinema_hall', 'start_time']