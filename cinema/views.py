from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Actor, Genre, CinemaHall, Movie
from .serializers import (
    ActorSerializer, GenreSerializer, CinemaHallSerializer, MovieSerializer
)



class GenreListCreateAPIView(APIView):
    """Endpoint para GET (lista) e POST (criação) de Gêneros."""
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailAPIView(APIView):
    """Endpoint para GET, PUT, PATCH, DELETE de um Gênero específico."""
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Actor: GenericViewSet com Mixins ---
class ActorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet compatível com Router, usando apenas os métodos dos Mixins."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


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
    """ModelViewSet fornece CRUD completo automaticamente."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
