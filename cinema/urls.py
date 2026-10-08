from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "genres/",
        GenreList.as_view(),
        name="genres-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genres-detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actors-list"),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actors-detail"
    ),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="cinema-hall-list",
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="cinema-hall-detail",
    ),
]
