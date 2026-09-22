"""Validate cinema resources and represent relations as IDs."""
from __future__ import annotations

from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    """Serialize genres and validate name uniqueness."""

    class Meta:
        model = Genre
        fields: tuple[str, ...] = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    """Serialize actors."""

    class Meta:
        model = Actor
        fields: tuple[str, ...] = ("id", "first_name", "last_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    """Serialize cinema halls."""

    class Meta:
        model = CinemaHall
        fields: tuple[str, ...] = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.ModelSerializer):
    """Serialize movies with primary-key lists for relations."""

    class Meta:
        model = Movie
        fields: tuple[str, ...] = (
            "id", "title", "description", "duration", "actors", "genres",
        )
