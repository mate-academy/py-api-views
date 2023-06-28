from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()

        serializer = GenreSerializer(genres, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = GenreSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = GenreSerializer(self.get_object(pk), data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = GenreSerializer(
            self.get_object(pk), data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
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
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
