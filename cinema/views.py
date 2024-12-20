from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin
)
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import (
    ActorSerializer, GenreSerializer,
    CinemaHallSerializer, MovieSerializer
)

from rest_framework.viewsets import ModelViewSet


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GenreDetail(APIView):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=204)


class CinemaHallViewSet(
    GenericViewSet, ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        actors = self.request.data.get("actors", [])
        genres = self.request.data.get("genres", [])
        movie = serializer.save()
        movie.actors.set(actors)
        movie.genres.set(genres)

    def perform_update(self, serializer):
        actors = self.request.data.get("actors", None)
        genres = self.request.data.get("genres", None)
        movie = serializer.save()
        if actors is not None:
            movie.actors.set(actors)
        if genres is not None:
            movie.genres.set(genres)
