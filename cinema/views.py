"""Class-based cinema API views."""
from __future__ import annotations

from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from cinema.models import Actor, CinemaHall, Genre, Movie
from cinema.serializers import (
    ActorSerializer, CinemaHallSerializer, GenreSerializer, MovieSerializer,
)


class GenreList(APIView):
    """List or create genres."""
    def get(self, request: Request) -> Response:
        """Return every genre."""
        serializer = GenreSerializer(Genre.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """Create a genre."""
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    """Retrieve, update, or delete a genre."""
    def get_object(self, pk: int) -> Genre:
        """Return a genre or HTTP 404."""
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        """Return a genre."""
        return Response(GenreSerializer(self.get_object(pk)).data)

    def put(self, request: Request, pk: int) -> Response:
        """Replace a genre."""
        serializer = GenreSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        """Partially update a genre."""
        serializer = GenreSerializer(
            self.get_object(pk), data=request.data, partial=True,
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
    """List or create actors."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request) -> Response:
        """Return every actor."""
        return self.list(request)

    def post(self, request: Request) -> Response:
        """Create an actor."""
        return self.create(request)


class ActorDetail(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, GenericAPIView,
):
    """Retrieve, update, or delete actors."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, pk: int) -> Response:
        """Return an actor."""
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
    mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet,
):
    """Provide cinema-hall CRUD actions."""
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Provide movie CRUD actions."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
