from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreList,
    ActorList,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = 'cinema'
router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahall")


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"), #
    path("actors/", ActorList.as_view(), name="actor-list"), #
    path("", include(router.urls)),
]
