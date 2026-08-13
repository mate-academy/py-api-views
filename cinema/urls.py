from django.urls import path, include

from .views import GenreAPIView, ActorListView, CinemaHallViewSet, MovieViewSet


app_name = "cinema"

urlpatterns = [
    path("actors/", ActorListView.as_view(), name="actor-list"),

    path("genres/", GenreAPIView.as_view(), name="genre-list"),

    path(
        "halls/",
        CinemaHallViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="hall-list",
    ),
    path(
        "halls/<int:pk>/",
        CinemaHallViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="hall-detail",
    ),

    path(
        "movies/",
        MovieViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="movie-list",
    ),
    path(
        "movies/<int:pk>/",
        MovieViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="movie-detail",
    ),
]
