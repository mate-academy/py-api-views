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
        title = validated_data.get("title", instance.title)
        description = validated_data.get("description", instance.description)
        duration = validated_data.get("duration", instance.duration)

        if (title != instance.title
                or description != instance.description
                or duration != instance.duration):
            instance.title = title
            instance.description = description
            instance.duration = duration
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
