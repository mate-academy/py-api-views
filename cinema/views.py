from django.http import HttpResponse, HttpRequest

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.response import Response
from rest_framework import status, mixins

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):
    def get(self, request: HttpRequest) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest) -> HttpResponse:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    @staticmethod
    def get_object(request: HttpRequest, pk: int) -> object:
        return get_object_or_404(Genre, id=pk)

    from rest_framework import status

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        genre = self.get_object(request, pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, pk: int) -> HttpResponse:
        bus = self.get_object(request, pk)
        serializer = GenreSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: HttpRequest, pk: int) -> HttpResponse:
        bus = self.get_object(request, pk)
        serializer = GenreSerializer(bus, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        genre = self.get_object(request, pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    ListModelMixin,
    CreateModelMixin,
    GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        return self.create(request, *args, **kwargs)


class ActorDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return self.retrieve(request=request, *args, **kwargs)

    def put(self, request, *args, **kwargs) -> HttpResponse:
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> HttpResponse:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> HttpResponse:
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
