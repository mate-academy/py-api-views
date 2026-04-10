from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.views import APIView

from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


# Genre
class GenreList(APIView):
    def get(self, request: Request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get(self, request: Request, pk: int) -> Response:
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Actor
class ActorList(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request) -> Response:
        serializer = self.get_serializer(self.get_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActorDetail(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, pk: int) -> Response:
        actor = get_object_or_404(Actor, pk=pk)
        serializer = self.get_serializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        actor = get_object_or_404(Actor, pk=pk)
        serializer = self.get_serializer(actor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        actor = get_object_or_404(Actor, pk=pk)
        serializer = self.get_serializer(actor, data=request.data, partial=True)

    def delete(self, request: Request, pk: int) -> Response:
        actor = get_object_or_404(Actor, pk=pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CinemaHall
class CinemaHallViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


# Movie
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
