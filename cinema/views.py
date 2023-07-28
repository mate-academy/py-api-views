from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics, mixins

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cinema.models import Movie, CinemaHall, Actor, Genre
from cinema.serializers import (
    MovieSerializer, CinemaHallSerializer,
    ActorSerializer, GenreSerializer
)


class MovieViewSet(ModelViewSet):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreList(APIView):

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(mixins.UpdateModelMixin, APIView):

    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genre = self.get_object(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = GenreSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        serializer = GenreSerializer(
            self.get_object(pk),
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
