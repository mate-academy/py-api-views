from django.urls import path

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
)

urlpatterns = [
    path(
        "movies/",
        MovieViewSet.as_view(
            actions={
                "get": "list",
                "post": "create"
            }
        ),
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        MovieViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="movie-detail"
    ),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "list",
                "post": "create"
            }
        ),
        name="actor-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="actor-list"
    ),
]

app_name = "cinema"
