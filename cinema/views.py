from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Actor, Genre, CinemaHall, Movie
from .serializers import ActorSerializer, GenreSerializer, CinemaHallSerializer, MovieSerializer


# ... GenreListCreateAPIView e GenreDetailAPIView (Mantidas, com get_object_or_404) ...


# --- Actor: GenericViewSet com Mixins (MÉTODO CORRETO) ---
class ActorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,  # Herda de ViewSet base
):
    """ViewSet compatível com Router, usando apenas os métodos dos Mixins."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # MÉTODOS HTTP (get, post, put, etc.) FORAM REMOVIDOS AQUI.


# --- CinemaHall: GenericViewSet ---
class CinemaHallViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


# --- Movie: ModelViewSet ---
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
