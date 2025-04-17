from rest_framework import serializers

from .models import (
    Movie,
    Genre,
    Actor,
    CinemaHall
)


class MovieSerializer(serializers.Serializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "actors", "genres"]

    def create(self, validated_data):
        try:
            actors = validated_data.pop("actors", [])
            genres = validated_data.pop("genres", [])
            movie = Movie.objects.create(**validated_data)
            movie.actors.set(actors)
            movie.genres.set(genres)
            return movie
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error creating movie: {str(e)}"}
            )

    def update(self, instance, validated_data):
        try:
            actors = validated_data.pop("actors", None)
            genres = validated_data.pop("genres", None)

            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            if actors is not None:
                instance.actors.set(actors)
            if genres is not None:
                instance.genres.set(genres)

            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error updating movie: {str(e)}"}
            )


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63)

    def create(self, validated_data):
        try:
            return Genre.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error creating genre: {str(e)}"}
            )

    def update(self, instance, validated_data):
        try:
            instance.name = validated_data.get("name", instance.name)
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error updating genre: {str(e)}"}
            )


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=63)
    last_name = serializers.CharField(max_length=63)

    def create(self, validated_data):
        try:
            return Actor.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error creating actor: {str(e)}"}
            )

    def update(self, instance, validated_data):
        try:
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
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error updating actor: {str(e)}"}
            )


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        try:
            return CinemaHall.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error creating cinema hall: {str(e)}"}
            )

    def update(self, instance, validated_data):
        try:
            instance.name = validated_data.get(
                "name",
                instance.name
            )
            instance.rows = validated_data.get(
                "rows",
                instance.rows
            )
            instance.seats_in_row = validated_data.get(
                "seats_in_row",
                instance.seats_in_row
            )
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(
                {"detail": f"Error updating cinema hall: {str(e)}"}
            )
