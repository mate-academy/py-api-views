from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Genre, Actor, CinemaHall, Movie
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


class GenreList(APIView):
    """List all genres or create a new one."""

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


class GenreDetail(APIView):
    """Retrieve, update, or delete a genre by id."""

    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """List all actors or create a new one."""

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ActorDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """Retrieve, update, or delete an actor by id."""

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for CinemaHall model."""

    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Full CRUD for Movie using ModelViewSet."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
