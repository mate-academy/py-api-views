from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail
)

CINEMA_HALL_LIST_ACTIONS = {"get": "list", "post": "create"}
CINEMA_HALL_DETAIL_ACTIONS = {
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
}

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CinemaHallList.as_view(CINEMA_HALL_LIST_ACTIONS),
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetail.as_view(CINEMA_HALL_DETAIL_ACTIONS),
        name="cinema-hall-detail"
    ),
]

app_name = "cinema"
