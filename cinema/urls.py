from django.urls import path

from cinema.views import (
    MovieViewSet,
    ActorDetailView,
    ActorListView,
    GenreDetailView,
    GenreListView,
    CinemaHallDetailView,
    CinemaHallListView,
)


movie_list = MovieViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path(
        "genres/",
        GenreListView.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetailView.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        ActorListView.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetailView.as_view(),
        name="actor-detail"
    ),
    path(
        "cinema-hall/",
        CinemaHallListView.as_view(),
        name="cinema-hall-list"
    ),
    path(
        "cinema-hall/<int:pk>/",
        CinemaHallDetailView.as_view(),
        name="cinema-hall-detail"
    ),

    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
