from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from cinema.models import Movie, Genre, Actor, CinemaHall, Screening
from cinema.serializers import MovieSerializer, GenreSerializer, ActorSerializer, CinemaHallSerializer, \
    ScreeningSerializer


class GenreList(APIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get_object(self, pk):
        return get_object_or_404(self.queryset, pk=pk)

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = self.serializer_class(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = self.serializer_class(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        serializer = self.serializer_class(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ScreeningViewSet(ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


