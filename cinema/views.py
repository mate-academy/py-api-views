from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from cinema.models import Genre, Actor, CinemaHall, Movie
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


class GenreAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            genre = get_object_or_404(Genre, pk=pk)
            serializer = GenreSerializer(genre)
        else:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def put(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CinemaHallViewSet(
    viewsets.GenericViewSet,
    generics.ListCreateAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def post(self, request):
        serializer = CinemaHallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        cinema_hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = CinemaHallSerializer(cinema_hall, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        cinema_hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = CinemaHallSerializer(cinema_hall, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
