from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    GenreSerializer,
    MovieSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genres_serializer = GenreSerializer(genres, many=True)

        return Response(genres_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        genres_serializer = GenreSerializer(data=request.data)
        if genres_serializer.is_valid():
            genres_serializer.save()
            return Response(
                genres_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            genres_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class GenreDetail(APIView):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre_serializer = GenreSerializer(genre)

        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genres_serializer = GenreSerializer(genre, data=request.data)
        if genres_serializer.is_valid():
            genres_serializer.save()
            return Response(genres_serializer.data)

        return Response(
            genres_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genres_serializer = GenreSerializer(
            genre, data=request.data, partial=True
        )
        if genres_serializer.is_valid():
            genres_serializer.save()
            return Response(genres_serializer.data)

        return Response(
            genres_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
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


class ActorDetail(
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

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
