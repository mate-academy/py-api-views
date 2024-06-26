from django.urls import path, include
from rest_framework import routers
from cinema import views
from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallList,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"
movie_list = MovieViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
movie_detail = MovieViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(actions={
        "get": "list",
        "post": "create"
    }), name="cinemahall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
    ), name="actor-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
