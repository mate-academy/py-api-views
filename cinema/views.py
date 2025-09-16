from rest_framework.generics import (
    GenericAPIView
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet
)

from django.shortcuts import get_object_or_404

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(
            genres,
            many=True
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = GenreSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(
            Genre,
            pk=pk
        )

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(
            genre,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(
            genre,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ActorList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ActorDetail(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.partial_update(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)


class CinemaHallViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
