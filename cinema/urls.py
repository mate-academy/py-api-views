from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
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

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    path("genres/", GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path("cinema_halls/", cinemahall_list, name="cinemahall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinemahall_detail,
        name="cinemahall-detail"
    ),

    path("", include(router.urls)),
]
