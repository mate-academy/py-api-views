from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView, GenreDetailAPIView,
    ActorViewSet, CinemaHallViewSet, MovieViewSet
)

router = DefaultRouter()
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Rotas para Genre (APIView)
    path("genres/", GenreListCreateAPIView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),

    # Inclui rotas do Router (actors, cinema_halls, movies)
    path("", include(router.urls)),
]
