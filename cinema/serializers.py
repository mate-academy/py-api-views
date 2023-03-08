from rest_framework import serializers

from cinema.models import Movie, Actor, Genre


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    actor = serializers.ManyRelatedField(child_relation=Actor)
    genre = serializers.ManyRelatedField(child_relation=Genre)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.actor = validated_data.get("actor", instance.actor)
        instance.genre = validated_data.get("genre", instance.genre)

        instance.save()

        return instance

