from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cinema.models import Movie, CinemaHall, Actor
from cinema.serializers import MovieSerializer, CinemaHallSerializer, ActorSerializer


class ActorListViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetailViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
