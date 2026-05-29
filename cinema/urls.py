from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    CinemaHallViewSet,
    GenreDetail,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
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
        "genres/",
        GenreList.as_view(),
        name="genre_list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre_detail"
    ),
    path(
        "cinema-halls/",
        CinemaHallViewSet.as_view({
            "get": "list",
            "post": "create"
        }),
        name="cinema_hall_list"
    ),
    path(
        "cinema-halls/<int:pk>/",
        CinemaHallViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name="cinema_hall_detail"
    ),
    path("", include(router.urls)),

]

app_name = "cinema"
