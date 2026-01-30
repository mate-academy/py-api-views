from rest_framework import status, mixins
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response

from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def list(self, request):
        cinema_halls = self.get_queryset()
        serializer = self.get_serializer(cinema_halls, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        cinema_hall = self.get_object()
        serializer = self.get_serializer(cinema_hall)
        return Response(serializer.data)

    def update(self, request, pk=None):
        cinema_hall = self.get_object()
        serializer = self.get_serializer(cinema_hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        cinema_hall = self.get_object()
        serializer = self.get_serializer(
            cinema_hall, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cinema_hall = self.get_object()
        cinema_hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
