from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSets,
)

movie_list = MovieViewSets.as_view(actions={
    "get": "list",
    "post": "create",
})

movie_detail = MovieViewSets.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinema-halls/",
        CinemaHallList.as_view(),
        name="cinema-hall-list"
    ),
    path(
        "cinema-halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema-hall-detail"
    ),
    path("movies/", movie_list, name="movie-list"),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail"
    ),
]

app_name = "cinema"
