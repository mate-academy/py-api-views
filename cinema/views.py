"""CRUD endpoints using four class-based DRF approaches."""
from __future__ import annotations

from django.db.models import QuerySet
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
    """Handle genre collection requests explicitly."""

    def get(self, request: Request) -> Response:
        serializer = GenreSerializer(Genre.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    """Retrieve, update, or delete a genre."""

    def get_object(self, pk: int) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        serializer = GenreSerializer(
            self.get_object(pk), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    """Connect collection requests to mixin actions."""

    queryset: QuerySet[Actor] = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request) -> Response:
        return self.list(request)

    def post(self, request: Request) -> Response:
        return self.create(request)


class ActorDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    """Connect detail requests to mixin actions."""

    queryset: QuerySet[Actor] = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, pk: int) -> Response:
        return self.retrieve(request, pk=pk)

    def put(self, request: Request, pk: int) -> Response:
        return self.update(request, pk=pk)

    def patch(self, request: Request, pk: int) -> Response:
        return self.partial_update(request, pk=pk)

    def delete(self, request: Request, pk: int) -> Response:
        return self.destroy(request, pk=pk)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Compose hall CRUD actions from mixins."""

    queryset: QuerySet[CinemaHall] = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Provide all movie CRUD actions."""

    queryset: QuerySet[Movie] = Movie.objects.prefetch_related(
        "actors", "genres"
    )
    serializer_class = MovieSerializer
