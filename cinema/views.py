from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class MovieDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk):
        movie = self.get_object(pk=pk)
        movie.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
