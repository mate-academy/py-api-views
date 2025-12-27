from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance


class ActorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    class Meta:
        model = Actor


class GenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    class Meta:
        model = Genre


class CinemaHallSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rows = serializers.IntegerField(default=0)
    seats_in_row = serializers.IntegerField(default=0)

    class Meta:
        model = CinemaHall
