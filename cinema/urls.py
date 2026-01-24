from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView, GenreDetailAPIView,
    ActorViewSet, CinemaHallViewSet, MovieViewSet
)

# Adicionado app_name para resolver o erro de ImproperlyConfigured anterior
app_name = 'cinema'

router = DefaultRouter()
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Rotas para Genre (APIView)
    path(
        "genres/",
        GenreListCreateAPIView.as_view(),
        name="genre_list_create"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetailAPIView.as_view(),
        name="genre-detail"
    ),

    # Inclui rotas do Router (actors, cinema_halls, movies)
    path("", include(router.urls)),
]
