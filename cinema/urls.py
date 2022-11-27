from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movie-set")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls-set")

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "cinema"
