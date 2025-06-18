from rest_framework import serializers
from .models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name",
                                                instance.last_name)
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get("seats_in_row",
                                                   instance.seats_in_row)
        instance.save()
        return instance


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField(min_value=1, max_value=500)
    release_date = serializers.DateField(required=False)
    rating = serializers.FloatField(required=False, allow_null=True)
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = ["id",
                  "title",
                  "description",
                  "duration",
                  "release_date",
                  "rating",
                  "actors",
                  "genres"]
        extra_kwargs = {
            "duration": {
                "min_value": 1,
                "max_value": 500
            },
            "rating": {
                "required": False,
                "allow_null": True
            }
        }

    def validate_duration(self, value):
        try:
            if isinstance(value, str):
                if not value.isdigit():
                    raise serializers.ValidationError(
                        "Duration must be a positive integer.")
                value = int(value)
            if not isinstance(value, (int, float)):
                raise serializers.ValidationError(
                    "Duration must be a positive integer.")
            if isinstance(value, (int, float)) and (value < 1 or value > 500):
                raise serializers.ValidationError(
                    "Duration must be between 1 and 500.")
            return value
        except (ValueError, TypeError):
            raise serializers.ValidationError(
                "Duration must be a positive integer between 1 and 500.")

    def validate(self, data):
        if "duration" in data:
            duration = data.get("duration")
            if duration is not None:
                data["duration"] = self.validate_duration(duration)
        return data

    def create(self, validated_data):
        actors = validated_data.pop("actors")
        genres = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        movie.genres.set(genres)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title",
                                            instance.title)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.duration = validated_data.get("duration",
                                               instance.duration)

        if "actors" in validated_data:
            instance.actors.set(validated_data["actors"])
        if "genres" in validated_data:
            instance.genres.set(validated_data["genres"])

        instance.save()
        return instance
