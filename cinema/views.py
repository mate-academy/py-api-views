from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from cinema.models import Movie, Actor, CinemaHall, Genre
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)
        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        genre_serializer = GenreSerializer(data=request.data)
        genre_serializer.is_valid(raise_exception=True)
        genre_serializer.save()
        return Response(genre_serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk):
        genre = self.get_object(pk)
        genre_serializer = GenreSerializer(genre)
        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = self.get_object(pk)
        genre_serializer = GenreSerializer(genre, data=request.data)
        genre_serializer.is_valid(raise_exception=True)
        genre_serializer.save()
        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        genre_serializer = GenreSerializer(
            genre,
            data=request.data,
            partial=True
        )
        genre_serializer.is_valid(raise_exception=True)
        genre_serializer.save()
        return Response(request.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
