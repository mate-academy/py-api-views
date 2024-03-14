from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(APIView):

    def get(self, request):
        gener = Genre.objects.all()
        serializer = GenreSerializer(gener, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk):
        gener = self.get_object(pk)
        serializer = GenreSerializer(gener)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        gener = self.get_object(pk)
        serializer = GenreSerializer(gener, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gener = self.get_object(pk)
        gener.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)