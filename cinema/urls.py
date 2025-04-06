from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    ActorDetailList,
    ActorList,
    CinemaHallDetailList,
    CinemaHallList,
    GenreDetailList,
    GenreList,
    MovieViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreDetailList.as_view(),
        name="genre-detail-list",
    ),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        ActorDetailList.as_view(),
        name="actor-detail-list",
    ),
    path(
        "cinema_halls/",
        CinemaHallList.as_view(),
        name="cinema-hall-list",
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetailList.as_view(),
        name="cinema-hall-detail-list",
    ),
]

app_name = "cinema"
