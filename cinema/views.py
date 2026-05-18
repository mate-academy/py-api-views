from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from cinema.models import Movie, Actor, Genre, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer)

from rest_framework.views import APIView
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import (ListModelMixin,
                                   CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet


class GenreList(APIView):
    def get(self, request, *args, **kwargs):
        genres = Genre.objects.prefetch_related("movies")
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializers = GenreSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, *args, **kwargs):
        genre = self.get_object(kwargs.get("pk"))
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        genre = self.get_object(kwargs.get("pk"))
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        genre = self.get_object(kwargs.get("pk"))
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        genre = self.get_object(kwargs.get("pk"))
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(GenericAPIView,
                ListModelMixin,
                CreateModelMixin):
    queryset = Actor.objects.prefetch_related("movies")
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            return self.create(request, *args, **kwargs)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetail(GenericAPIView,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin):
    queryset = Actor.objects.prefetch_related("movies")
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        actor = Actor.objects.get(pk=kwargs.get("pk"))
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            return self.update(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        actor = Actor.objects.get(pk=kwargs.get("pk"))
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid():
            return self.partial_update(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(GenericViewSet,
                        ListCreateAPIView,
                        RetrieveUpdateDestroyAPIView):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("actors", "genres")
    serializer_class = MovieSerializer
