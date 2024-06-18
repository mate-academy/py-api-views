from rest_framework.response import Response
from rest_framework import (
    status,
    generics,
    mixins,
    viewsets,
)
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall,
)
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):

    def post(self, request) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreDetail(APIView):

    def get_genre(self, pk):
        genre = get_object_or_404(Genre, pk=pk)
        return genre

    def get(self, request, pk) -> Response:
        serializer = GenreSerializer(self.get_genre(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk) -> Response:
        serializer = GenreSerializer(self.get_genre(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk) -> Response:
        serializer = GenreSerializer(self.get_genre(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk) -> Response:
        self.get_genre(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class ActorDetail(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)


class CinemaHallList(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class CinemaHallViewSet(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
