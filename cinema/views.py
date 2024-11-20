from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView, GenericAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import ActorSerializer, GenreSerializer, \
    CinemaHallSerializer, MovieSerializer


class GenreList(APIView):
    """
    Handles listing all genres and creating a new genre.
    """
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    """
    Handles retrieving, updating, or deleting a single genre.
    """
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        """
        Handle partial update for Genre.
        """
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(ListCreateAPIView):
    """
    Handles listing all actors and creating a new actor.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a single actor.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    """
    Handles CRUD operations for the Movie model.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorGenericAPIView(GenericAPIView):
    """
    Handles CRUD operations for the Actor model.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        actors = self.get_queryset()
        serializer = self.get_serializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CinemaHallViewSet(GenericViewSet):
    """
    Handles CRUD operations for the CinemaHall model.
    """
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def list(self, request):
        halls = self.get_queryset()
        serializer = self.get_serializer(halls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = self.get_serializer(hall)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = self.get_serializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        hall = get_object_or_404(CinemaHall, pk=pk)
        serializer = self.get_serializer(hall, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        hall = get_object_or_404(CinemaHall, pk=pk)
        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieModelViewSet(ModelViewSet):
    """
    Handles CRUD operations for the Movie model.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
