from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 # Para consistência no GenreDetailAPIView
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
        # Usando get_object_or_404 para consistência
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) # Adicionando status explícito
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) # Adicionando status explícito
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Actor: GenericViewSet com Mixins (Corrigido para herdar de viewsets.GenericViewSet) ---
class ActorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet  # CORREÇÃO: Herdar de viewsets.GenericViewSet
):
    """Combina todos os mixins necessários para CRUD completo e é compatível com Router."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    # Implementação dos métodos HTTP para rotear para os mixins
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
