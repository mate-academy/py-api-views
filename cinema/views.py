from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets

from django.shortcuts import get_object_or_404

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


# @api_view(["GET", "POST"])
# def movie_list(request: HttpRequest) -> Response:
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request: HttpRequest, pk: int) -> Response:
#     movie = get_object_or_404(Movie, pk=pk)
#
#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "PUT":
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )
#
#     if request.method == "DELETE":
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(APIView):
    def get(self, request: HttpRequest) -> Response:
        genre_list = Genre.objects.all()
        serializer = GenreSerializer(genre_list, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: HttpRequest) -> Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get_object(self, pk: int) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: HttpRequest, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: HttpRequest, pk: int) -> Response:
        serializer = GenreSerializer(
            self.get_object(pk=pk),
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, pk: int) -> Response:
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class ActorDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
