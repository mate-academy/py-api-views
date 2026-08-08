from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    CreateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class GenreList(APIView):
    def get(self, request: Request):
        movies = Genre.objects.all()
        serializer = GenreSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk: int) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    ListCreateAPIView,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def patch(self, request: Request, pk, *args, **kwargs):
        return self.partial_update(request, pk, *args, **kwargs)

    def put(self, request: Request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request: Request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


class CinemaHallViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
