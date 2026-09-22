"""Class-based API views for cinema resources."""

from __future__ import annotations

from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Actor, CinemaHall, Genre, Movie
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer,
)


class GenreList(APIView):
    """List genres or create a genre."""

    def get(self, request: Request) -> Response:
        """Return every genre."""
        serializer = GenreSerializer(Genre.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """Create a genre from the request data."""
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    """Retrieve, update, or delete one genre."""

    def get_object(self, pk: int) -> Genre:
        """Get the requested genre or raise a 404 error."""
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        """Return one genre."""
        serializer = GenreSerializer(self.get_object(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """Replace a genre."""
        serializer = GenreSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        """Partially update a genre."""
        serializer = GenreSerializer(
            self.get_object(pk), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        """Delete a genre."""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    """List actors or create an actor."""

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request) -> Response:
        """Return every actor."""
        return self.list(request)

    def post(self, request: Request) -> Response:
        """Create an actor."""
        return self.create(request)


class ActorDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    """Retrieve, update, or delete one actor."""

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, pk: int) -> Response:
        """Return one actor."""
        return self.retrieve(request, pk=pk)

    def put(self, request: Request, pk: int) -> Response:
        """Replace an actor."""
        return self.update(request, pk=pk)

    def patch(self, request: Request, pk: int) -> Response:
        """Partially update an actor."""
        return self.partial_update(request, pk=pk)

    def delete(self, request: Request, pk: int) -> Response:
        """Delete an actor."""
        return self.destroy(request, pk=pk)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Provide complete CRUD operations for cinema halls."""

    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Provide complete CRUD operations for movies."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
