from django.urls import path

from cinema.views import (
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    movie_list,
    movie_detail
)

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})


cinema_halls_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_halls_list, name="cinema-halls-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_halls_detail,
        name="cinema-halls-detail"
    ),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
