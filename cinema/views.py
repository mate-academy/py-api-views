from rest_framework import viewsets
from cinema.models import Movie, Actor
from cinema.serializers import MovieSerializer, ActorSerializer, GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related("genres").prefetch_related("actors")
    serializer_class = MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.prefetch_related("movies")
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.select_related("movies")
    serializer_class = GenreSerializer

