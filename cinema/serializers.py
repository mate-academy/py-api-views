from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "second_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:
        actors_data = validated_data.pop("actors")
        genres_data = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)

        for actor_data in actors_data:
            actor = Actor.objects.get(pk=actor_data["id"])
            movie.actors.add(actor)

        for genre_data in genres_data:
            genre = Genre.objects.get(pk=genre_data["id"])
            movie.genres.add(genre)
        movie.save()
        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        actors_data = validated_data.get("actors", [])
        genres_data = validated_data.get("genres", [])
        instance.actors.clear()
        instance.genres.clear()

        for actor_data in actors_data:
            actor = Actor.objects.get(pk=actor_data["id"])
            instance.actors.add(actor)

        for genre_data in genres_data:
            genre = Genre.objects.get(pk=genre_data["id"])
            instance.genres.add(genre)

        instance.save()
        return instance
