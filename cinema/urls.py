from django.urls import path

from cinema.views import (
    GenreDetail,
    GenreList,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

cinemahall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

movie_list = MovieViewSet.as_view(
    actions={"get": "list", "post": "create"}
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
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinemahall_list, name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinemahall_detail,
        name="cinema-hall-detail"
    ),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
