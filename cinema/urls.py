from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

cinema_hall_list = CinemaHallViewSet.as_view(
    {"get": "list", "post": "create", }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

movies_list_vs = MovieViewSet.as_view(
    {"get": "list", "post": "create"}
)
movies_detail_vs = MovieViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("movies_vs/", movies_list_vs, name="movie-list-vs"),
    path("movies_vs/<int:pk>/", movies_detail_vs, name="movie-detail-vsroute"),
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_hall/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_hall/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail",
    ),
]

app_name = "cinema"
