from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin
)
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, request, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genre = self.get_object(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = self.get_object(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    generics.GenericAPIView
):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActorDetail(generics.GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk):
        queryset = self.queryset.objects.get(pk=pk)
        serializer = self.get_serializer_class()(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = self.queryset.get(pk=pk)
        serializer = self.get_serializer_class()(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        queryset = self.queryset(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CinemaHallList(generics.ListCreateAPIView):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class CinemaHallDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    viewsets.ModelViewSet
):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
