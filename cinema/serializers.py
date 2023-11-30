from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), required=False, many=True)
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), required=False, many=True)

    def create(self, validated_data):
        actors_data = validated_data.pop("actors", [])
        genres_data = validated_data.pop("genres", [])

        movie = Movie.objects.create(**validated_data)

        movie.actors.set(actors_data)
        movie.genres.set(genres_data)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.description = validated_data.get("description",
                                                  instance.description)
        actors_data = validated_data.get("actors", [])
        genres_data = validated_data.get("genres", [])

        if actors_data:
            instance.actors.set(actors_data)
        if genres_data:
            instance.genres.set(genres_data)

        instance.save()

        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"
