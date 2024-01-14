from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (MovieSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get(self, request, pk):
        try:
            genres = Genre.objects.get(id=pk)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genres)
        return Response(data=serializer.data)

    def put(self, request, pk):
        genres = Genre.objects.get(id=pk)
        serializer = GenreSerializer(genres, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, pk):
        try:
            Genre.objects.get(id=pk).delete()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        genres = Genre.objects.get(id=pk)
        serializer = GenreSerializer(genres, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
