from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView

from .models import Genre, Actor, CinemaHall, Movie
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class ActorView(generics.GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallView(viewsets.GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
