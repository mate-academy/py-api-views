from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie
)
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer
)


class GenreList(APIView):
    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, id=pk)

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

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


class CinemaHallViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CinemaHall.objects.all()
        serializer = CinemaHallSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CinemaHallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        cinema_hall = CinemaHall.objects.get(id=pk)
        serializer = CinemaHallSerializer(cinema_hall)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        cinema_hall = CinemaHall.objects.get(id=pk)
        serializer = CinemaHallSerializer(cinema_hall, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def partial_update(self, request, pk):
        cinema_hall = CinemaHall.objects.get(id=pk)
        serializer = CinemaHallSerializer(
            cinema_hall,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        cinema_hall = CinemaHall.objects.get(id=pk)
        cinema_hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
