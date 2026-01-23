from django.urls import path, include
from rest_framework.routers import DefaultRouter # Importação necessária (F821)
from .views import (
    GenreListCreateAPIView, GenreDetailAPIView,
    ActorViewSet, CinemaHallViewSet, MovieViewSet # Nomes das Views corrigidos
)

router = DefaultRouter()
# Registrando sem prefixo na string, para que o path pai adicione 'cinema/'
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Rotas para Genre (APIView)
    path("genres/", GenreListCreateAPIView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),

    # Rotas do Router (serão prefixadas com /api/cinema/ + o caminho aqui)
    path("", include(router.urls)), # Inclui as rotas de actors, cinema_halls, movies
]
