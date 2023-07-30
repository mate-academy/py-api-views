from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)

movie_router = routers.DefaultRouter()
movie_router.register("movies", MovieViewSet)

cinema_hall_router = routers.DefaultRouter()
cinema_hall_router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(movie_router.urls)),
    path("", include(cinema_hall_router.urls)),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    )
]

app_name = "cinema"
