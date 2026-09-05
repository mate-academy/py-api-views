from django.urls import path

from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet, )

urlpatterns = [
    path("movies/", MovieViewSet.as_view({
        "get": "list",
        "post": "create",
    }), name="movie-list"),
    path("movies/<int:pk>/", MovieViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }), name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view({
        "get": "list",
        "post": "create",
    }), name="cinema_hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }), name="cinema_hall-detail"),
]

app_name = "cinema"
