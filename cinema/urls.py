from django.urls import path, include
from rest_framework import routers
from cinema.views import (MovieView,
                          CinemaHallView,
                          GenreDetail,
                          GenreList,
                          ActorDetail,
                          ActorList)

router = routers.DefaultRouter()
router.register("movies", MovieView)


urlpatterns = [
    path("movies/", include(router.urls), name="movie-list"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinemahalls/", CinemaHallView.as_view(actions={
        "get": "list",
        "post": "create",
    }), name="cinema-hall-list"),
    path("cinemahalls/<int:pk>/", CinemaHallView.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
        "patch": "partial_update",
    }), name="cinema-hall-detail"),
]

app_name = "cinema"
