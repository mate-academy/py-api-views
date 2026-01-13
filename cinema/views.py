from rest_framework import viewsets

from cinema.models import Movie
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    ActorSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
