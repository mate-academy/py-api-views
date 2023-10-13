from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)

from django.shortcuts import get_object_or_404

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class GenreList(APIView):
    def get(self, request: Request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serialized_data = GenreSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(
                serialized_data.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
        )


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        genre_object = self.get_object(pk=pk)
        serializer = GenreSerializer(genre_object)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        genre_object = self.get_object(pk=pk)
        serializer = GenreSerializer(genre_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        genre_object = self.get_object(pk=pk)
        serializer = GenreSerializer(genre_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        genre_object = self.get_object(pk=pk)
        genre_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class ActorDetail(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
