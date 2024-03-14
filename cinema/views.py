from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets

from rest_framework.views import APIView

from cinema.models import Movie, Actor, Genre, CinemaHall
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer,
)


class GenreListView(APIView):

    @staticmethod
    def get(request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request) -> Response:
        genres = Genre.objects.all()
        serializer = MovieSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreDetailView(APIView):
    @staticmethod
    def get_object(pk: int) -> Movie:
        return Genre.objects.get(pk=pk)

    def get(self, request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk: int) -> Response:
        serializer = GenreSerializer(
            self.get_object(pk), data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorListView(
    generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class ActorDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(self, request, *args, **kwargs)


class CinemaListView(generics.ListCreateAPIView):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class CinemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
