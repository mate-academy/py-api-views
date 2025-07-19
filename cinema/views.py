from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Genre, Actor, CinemaHall, Movie
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk):
        genre = self.get_object(pk)
        if not genre:
            return Response({"error": "Genre not found"}, status=404)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        if not genre:
            return Response({"error": "Genre not found"}, status=404)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        if not genre:
            return Response({"error": "Genre not found"}, status=404)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        if not genre:
            return Response({"error": "Genre not found"}, status=404)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# CinemaHall views using GenericViewSet
class CinemaHallViewSet(viewsets.GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def list(self, request):
        """Get a list of all cinema halls"""
        halls = self.get_queryset()
        serializer = self.get_serializer(halls, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new cinema hall"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Get a specific cinema hall by ID"""
        try:
            hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response(
                {"error": "Cinema hall not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(hall)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Update a cinema hall completely"""
        try:
            hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response(
                {"error": "Cinema hall not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(hall, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Update a cinema hall partially"""
        try:
            hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response(
                {"error": "Cinema hall not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(hall, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Delete a cinema hall"""
        try:
            hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response(
                {"error": "Cinema hall not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Movie views using ModelViewSet
class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset for Movie instances that provides all standard actions:
    list, create, retrieve, update, partial_update, destroy
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
