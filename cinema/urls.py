from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreListCreateAPIView,
    GenreDetailAPIView,
    ActorListCreateAPIView,
    ActorDetailAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Genre endpoints
    path("genres/", GenreListCreateAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),

    # Actor endpoints
    path("actors/", ActorListCreateAPIView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailAPIView.as_view(), name="actor-detail"),

    # CinemaHall + Movie (через router)
    path("", include(router.urls)),
]
