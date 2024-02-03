from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

cinemahall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("halls/", cinemahall_list, name="hall-list"),
    path("halls/<int:pk>/", cinemahall_detail, name="hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
