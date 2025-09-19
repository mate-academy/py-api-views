from django.http import HttpRequest
from rest_framework import viewsets, status
from rest_framework import views
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins


from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer
)


class ActorList(
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetail(
    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: HttpRequest, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request: HttpRequest, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: HttpRequest, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GenreList(views.APIView):
    @staticmethod
    def get(request: HttpRequest) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request: HttpRequest) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(views.APIView):
    @staticmethod
    def get_object(pk: int) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: HttpRequest, pk: int) -> Response:
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, pk: int) -> Response:
        genre = self.get_object(pk)

        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: HttpRequest, pk: int) -> Response:
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: HttpRequest, pk: int) -> Response:
        genre = self.get_object(pk)
        genre.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,

):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
