from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.exceptions import NotFound

from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer
)


class GenreList(APIView):
    def get(self, request):
        queryset = Genre.objects.all()
        genre_serializer = GenreSerializer(queryset, many=True)
        return Response(genre_serializer.data)

    def post(self, request):
        genre_serializer = GenreSerializer(data=request.data)

        if genre_serializer.is_valid():
            genre_serializer.save()
            return Response(
                genre_serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(genre_serializer.errors, status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    @staticmethod
    def _get_object(pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise NotFound(f"Genre with pk: {pk}, does not exist.")

    def get(self, request, pk):
        serializer = GenreSerializer(self._get_object(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = GenreSerializer(self._get_object(pk),
                                     data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        serializer = GenreSerializer(
            self._get_object(pk),
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self._get_object(pk).delete()
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
