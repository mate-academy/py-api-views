from django.shortcuts import get_object_or_404
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer
)


class GenreList(APIView):
    model = Genre
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):
        movies = self.model.objects.all()
        serializer = self.serializer_class(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class GenreDetail(APIView):
    model = Genre
    serializer_class = GenreSerializer

    def get_object(self, pk: int):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        serializer = self.serializer_class(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        serializer = self.serializer_class(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        serializer = self.serializer_class(
            movie,
            data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        movie.delete()
        return Response(
            {"message": "Movie deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )


class ActorList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
