from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import Movie, Genre, Actor, CinemaHall
from .serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk):
        serializer = GenreSerializer(self.get_object(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = GenreSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        serializer = GenreSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
