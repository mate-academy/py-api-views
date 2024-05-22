from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor_detail"
    ),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre_detail"
    ),
    path(
        "cinema_halls/",
        cinema_hall_list,
        name="cinema_hall_list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall_list"
    ),
]
