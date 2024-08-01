from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    MovieViewSet
)

cinema_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

cinema_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

movie_router = routers.DefaultRouter()
movie_router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(movie_router.urls)),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinema_halls/",
        cinema_list,
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_detail,
        name="cinema-hall-detail"
    ),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    )
]

app_name = "cinema"
