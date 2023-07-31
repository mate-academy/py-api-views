from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView


from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)

        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        genre_serializer = GenreSerializer(data=request.data)

        if genre_serializer.is_valid():
            genre_serializer.save()
            return Response(
                genre_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            genre_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class GenreDetail(APIView):
    def get_object(self, pk):
        genre = Genre.objects.filter(pk=pk).first()
        if genre is None:
            raise NotFound(f"Genre with ID: {pk}, does not exist")
        return genre

    def get(self, request, pk):
        genre = self.get_object(pk)
        genre_serializer = GenreSerializer(genre)

        return Response(genre_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = self.get_object(pk)
        genre_serializer = GenreSerializer(instance=genre, data=request.data)

        if genre_serializer.is_valid():
            genre_serializer.save()
            return Response(genre_serializer.data, status=status.HTTP_200_OK)

        return Response(
            genre_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_object(self):
        pk = self.kwargs.get("pk")
        manufacturer = Actor.objects.filter(pk=pk).first()
        if manufacturer is None:
            raise NotFound(f"Actor with ID: {pk}, does not exist")
        return manufacturer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_object(self):
        pk = self.kwargs.get("pk")
        cinema_hall = CinemaHall.objects.filter(pk=pk).first()
        if cinema_hall is None:
            raise NotFound(f"Cinema Hall with ID: {pk}, does not exist")
        return cinema_hall


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_object(self):
        pk = self.kwargs.get("pk")
        movie = Movie.objects.filter(pk=pk).first()
        if movie is None:
            raise NotFound(f"Movie with ID: {pk}, does not exist")
        return movie
