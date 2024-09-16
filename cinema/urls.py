from django.urls import path
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    MovieViewSet
)

cinemahall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

cinemahall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

router = routers.SimpleRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),

    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),

    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list"
    ),

    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),

    path(
        "cinema_halls/",
        cinemahall_list,
        name="cinema-hall-list"
    ),

    path(
        "cinema_halls/<int:pk>/",
        cinemahall_detail,
        name="cinema-hall-detail"
    ),

] + router.urls

app_name = "cinema"
