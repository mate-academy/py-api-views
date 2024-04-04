from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

    name = serializers.CharField(max_length=100)

    def create(self: Genre, validated_data: dict) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self: Genre, instance: Genre.objects,
               validated_data: dict) -> Genre:
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self: Actor, validated_data: dict) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self: Actor, instance: Actor.objects,
               validated_data: dict) -> Actor:
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"

    name = serializers.CharField(max_length=100)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self: CinemaHall, validated_data: dict) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(self: CinemaHall, instance: CinemaHall.objects,
               validated_data: dict) -> CinemaHall:
        instance.name = validated_data.get(
            "name", instance.name)
        instance.rows = validated_data.get(
            "rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()
        return instance
