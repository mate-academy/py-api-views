from rest_framework import viewsets, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Actor, Genre, CinemaHall, Movie
from .serializers import ActorSerializer, GenreSerializer, CinemaHallSerializer, MovieSerializer

# --- Genre: APIView ---
class GenreListCreateAPIView(APIView):
    """Endpoint para GET (lista) e POST (criação) de Gêneros."""
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenreDetailAPIView(APIView):
    """Endpoint para GET, PUT, PATCH, DELETE de um Gênero específico."""
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Actor: GenericAPIView com Mixins ---
class ActorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """Combina todos os mixins necessários para CRUD completo."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# --- CinemaHall: GenericViewSet ---
class CinemaHallViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    """Usa GenericViewSet que herda de ViewSet e combina com mixins."""
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

# --- Movie: ModelViewSet ---
class MovieViewSet(viewsets.ModelViewSet):
    """ModelViewSet fornece CRUD completo automaticamente."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
