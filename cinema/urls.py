from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "cinema-hall/",
        CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"}),
        name="hall-list"
    ),
    path(
        "cinema-hall/<pk>/",
        CinemaHallViewSet.as_view(actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name="hall-detail"
    ),
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list",)
]

app_name = "cinema"
