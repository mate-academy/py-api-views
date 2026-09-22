"""Serializers for cinema API resources."""

from __future__ import annotations

from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    """Serialize Genre instances."""

    class Meta:
        """Serializer metadata."""

        model = Genre
        fields: tuple[str, ...] = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    """Serialize Actor instances."""

    class Meta:
        """Serializer metadata."""

        model = Actor
        fields: tuple[str, ...] = ("id", "first_name", "last_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    """Serialize CinemaHall instances."""

    class Meta:
        """Serializer metadata."""

        model = CinemaHall
        fields: tuple[str, ...] = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.ModelSerializer):
    """Serialize Movie relations as primary-key lists."""

    class Meta:
        """Serializer metadata."""

        model = Movie
        fields: tuple[str, ...] = (
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres",
        )
        extra_kwargs: dict[str, dict[str, bool]] = {
            "actors": {"required": False},
            "genres": {"required": False},
        }
