from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=63, required=True, allow_blank=False)

    class Meta:
        model = Genre
        fields = "__all__"

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        instance.save()

        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63, required=True)
    rows = serializers.IntegerField(required=True)
    seats_in_row = serializers.IntegerField(required=True)

    class Meta:
        model = CinemaHall
        fields = "__all__"

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row)

        instance.save()

        return instance


class ActorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=63)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model = Actor
        fields = "__all__"

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)

        instance.save()

        return instance


class MovieActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    actors = MovieActorSerializer(many=True, required=False, partial=True)
    genres = MovieGenreSerializer(many=True, required=False, partial=True)

    class Meta:
        model = Movie
        fields = "__all__"
