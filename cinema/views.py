from rest_framework import viewsets, mixins, generics
from cinema.models import Movie, CinemaHall, Actor
from cinema.serializers import MovieSerializer, CinemaHallSerializer


class MovieModelViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaHallViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
