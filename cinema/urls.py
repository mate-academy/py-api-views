from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView, GenreDetailAPIView,
    ActorViewSet, CinemaHallViewSet, MovieViewSet
)

# ADICIONAR ESTA LINHA
app_name = 'cinema'

router = DefaultRouter(
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Rotas para Genre (APIView)
    path(
        "genres/",
        GenreListCreateAPIView.as_view(),
        name="genre_list_create"  # Nome alterado para encurtar
    ),
    path(
        "genres/<int:pk>/",
        GenreDetailAPIView.as_view(),
        name="genre-detail"
    ),  # Linhas ajustadas para não quebrar E501

    # Inclui rotas do Router (actors, cinema_halls, movies)
    path("", include(router.urls)),
]
