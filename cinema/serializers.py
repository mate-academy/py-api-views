from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall
)


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        required=False,
        many=True
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        required=False,
        many=True
    )

    class Meta:
        model = Movie
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=255,
        validators=[
            UniqueValidator(
                queryset=Genre.objects.all()
            )
        ]
    )

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance
