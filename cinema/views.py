from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class MovieList(APIView):

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):

    def get(self, request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        serializer = MovieSerializer(get_object_or_404(Movie, pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk: int) -> Response:
        get_object_or_404(Movie, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreList(APIView):

    def get(self, request: Request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):

    def get(self, request: Request, pk: int) -> Response:
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk: int) -> Response:
        get_object_or_404(Genre, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ActorList(APIView):

    def get(self, request: Request) -> Response:
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetail(APIView):

    def get(self, request: Request, pk: int) -> Response:
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        actors = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk: int) -> Response:
        get_object_or_404(Genre, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CinemaHallList(APIView):

    def get(self, request: Request) -> Response:
        halls = CinemaHall.objects.all()
        serializer = CinemaHallSerializer(halls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = CinemaHallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CinemaHallDetail(APIView):

    def get(self, request: Request, pk: int) -> Response:
        hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = CinemaHallSerializer(hall)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = CinemaHallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request,  pk: int) -> Response:
        get_object_or_404(CinemaHall, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
