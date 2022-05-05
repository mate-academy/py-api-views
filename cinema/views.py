from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets

from rest_framework.views import APIView

from cinema.models import Movie, Actor, Genre, CinemaHall
from cinema.serializers import MovieSerializer, ActorSerializer, \
    GenreSerializer, CinemahallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorList(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ActorDetail(APIView):
    def get_object(self, pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        actor = self.get_object(pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView
                ):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenreDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemahallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemahallSerializer
