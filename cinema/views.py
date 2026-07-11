from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from cinema.models import Actor
from cinema.models import CinemaHall
from cinema.models import Genre
from cinema.models import Movie
from cinema.serializers import ActorSerializer
from cinema.serializers import CinemaHallSerializer
from cinema.serializers import GenreSerializer
from cinema.serializers import MovieSerializer


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(
            genre,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
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
    GenericAPIView,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
