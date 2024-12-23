from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from django.http import Http404
from django.shortcuts import get_object_or_404

from cinema.models import Genre, Actor, CinemaHall, Movie
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


class GenreList(APIView):
    def get(self, request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk: int) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk: int) -> Response:
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk: int) -> Response:
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk: int) -> Response:
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk: int) -> Response:
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request) -> Response:
        return self.list(request)

    def post(self, request) -> Response:
        return self.create(request)


class ActorDetail(
    generics.GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk: int) -> Response:
        return self.retrieve(request, pk)

    def put(self, request, pk: int) -> Response:
        return self.update(request, pk)

    def patch(self, request, pk: int) -> Response:
        return self.partial_update(request, pk)

    def delete(self, request, pk: int) -> Response:
        return self.destroy(request, pk)


class CinemaHallViewSet(
    viewsets.GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
