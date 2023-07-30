from rest_framework import status, generics, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall
)
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        genres = Genre.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)
        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request: Request) -> Response:
        genre_serializer = GenreSerializer(data=request.data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return Response(
                genre_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class GenreDetail(APIView):
    @staticmethod
    def get_object_or_404_(pk: int) -> Genre | Response:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        genre = self.get_object_or_404_(pk)
        genre_serializer = GenreSerializer(genre)
        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        genre = self.get_object_or_404_(pk)
        genre_serializer = GenreSerializer(genre, data=request.data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return Response(genre_serializer.data, status=status.HTTP_200_OK)
        return Response(genre_serializer.data,
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int) -> Response:
        genre = self.get_object_or_404_(pk)
        genre_serializer = GenreSerializer(
            genre, data=request.data, partial=True
        )
        if genre_serializer.is_valid():
            genre_serializer.save()

            return Response(genre_serializer.data, status=status.HTTP_200_OK)

        return Response(
            genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request: Request, pk: int) -> Response:
        genre = self.get_object_or_404_(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
