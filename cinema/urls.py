from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)

router = routers.SimpleRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres"),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genres_detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor_list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor_detail"
    ),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "list",
                "post": "create"
            }
        ),
        name="cinema_hall_list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "patch": "partial_update",
                "put": "update",
                "delete": "destroy"
            }
        ),
        name="cinema_hall_detail"
    ),

    path("", include(router.urls), name="movies"),

]

app_name = "cinema"
