from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cinema.models import Movie, CinemaHall
from cinema.serializers import MovieSerializer, CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()
