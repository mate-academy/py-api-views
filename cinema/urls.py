from django.urls import path

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
)

movie_list = MovieViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
movie_detail = MovieViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

cinema_hall_list = CinemaHallViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list",
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail",
    ),
    path(
        "cinema_halls/",
        cinema_hall_list,
        name="cinema-hall-list",
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail",
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list",
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail",
    ),
    path(
        "movies/",
        movie_list,
        name="movie-list",
    ),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail",
    ),
]

app_name = "cinema"
