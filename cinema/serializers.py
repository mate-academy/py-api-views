from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    def create(self, validated_data):
        actors_data = validated_data.pop("actors", [])
        genres_data = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)
        movie.genres.add(*genres_data)
        movie.actors.add(*actors_data)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        actors_data = validated_data.get("actors", None)
        if actors_data is not None:
            instance.actors.set(actors_data)

        genres_data = validated_data.get("genres", None)
        if genres_data is not None:
            instance.genres.set(genres_data)

        instance.save()

        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")

    def validate_rows(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Rows must be greater than zero.")
        return value

    def validate_seats_in_row(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Seats in row must be greater than zero.")
        return value
