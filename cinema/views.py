from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from cinema.models import Actor, CinemaHall, Genre, Movie
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(APIView):
    def get(self, request):
        if request.method == "GET":
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.method == "POST":
            serializer = GenreSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.erros,
                            status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk):
        if request.method == "GET":
            serializer = GenreSerializer(self.get_object(pk))
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if request.method == "PUT":
            serializer = GenreSerializer(self.get_object(pk),
                                         data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if request.method == "PATCH":
            serializer = GenreSerializer(self.get_object(pk),
                                         data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            return Response(serializer.erros,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if request.method == "DELETE":
            self.get_object(pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ActorDetail(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, partial=True, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallViewSet(
    viewsets.GenericViewSet,
    generics.ListCreateAPIView,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
