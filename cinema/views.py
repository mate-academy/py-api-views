from rest_framework import mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Actor, Genre, CinemaHall, Movie
from .serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
)


# ------ Genre via APIView ------

class GenreListCreateAPIView(APIView):
    def get(self, request):
        qs = Genre.objects.all()
        serializer = GenreSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetailAPIView(APIView):
    def get_object(self, pk: int) -> Genre:
        return Genre.objects.get(pk=pk)

    def get(self, request, pk: int):
        serializer = GenreSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk: int):
        obj = self.get_object(pk)
        serializer = GenreSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk: int):
        obj = self.get_object(pk)
        serializer = GenreSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk: int):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------ Actor via GenericAPIView + mixins ------

class ActorListCreateAPIView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetailAPIView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk: int, *args, **kwargs):
        return self.retrieve(request, pk=pk, *args, **kwargs)

    def put(self, request, pk: int, *args, **kwargs):
        return self.update(request, pk=pk, *args, **kwargs)

    def patch(self, request, pk: int, *args, **kwargs):
        return self.partial_update(request, pk=pk, *args, **kwargs)

    def delete(self, request, pk: int, *args, **kwargs):
        return self.destroy(request, pk=pk, *args, **kwargs)


# ------ CinemaHall via GenericViewSet + mixins ------

class CinemaHallViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


# ------ Movie via ModelViewSet ------

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres").all()
    serializer_class = MovieSerializer
