from django.http import Http404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Genre, Actor, CinemaHall
from .serializers import MovieSerializer, GenreSerializer, \
    ActorSerializer, CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    @staticmethod
    def get_instance(pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genre = self.get_instance(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_instance(pk)
        serializer = GenreSerializer(genre, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        genre = self.get_instance(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_instance(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, generics.GenericAPIView):
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


class CinemaHallViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
