from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import views
from rest_framework.response import Response

from cinema.models import (
    Movie,
    Actor,
    CinemaHall,
    Genre
)
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(views.APIView):
    def get(self, request):
        objects = Genre.objects.all()
        serializer = GenreSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(views.APIView):
    def get(self, request, pk):
        genre = generics.get_object_or_404(Genre, id=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = generics.get_object_or_404(Genre, id=pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        genre = generics.get_object_or_404(Genre, id=pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        genre = generics.get_object_or_404(Genre, id=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ActorDetail(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)


class CinemaHallViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
