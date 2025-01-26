from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreListAPIView,
    GenreDetailAPIView,
    ActorListApiView,
    ActorDetailApiView,
    CinemaHallApiViewSet,
    MovieApiViewSet
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallApiViewSet, basename="cinema_hall")
router.register("movies", MovieApiViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreListAPIView.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"
    ),
    path("actors/", ActorListApiView.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/", ActorDetailApiView.as_view(), name="actor-detail"
    ),
    path("", include(router.urls)),
]

namespace = "cinema"
