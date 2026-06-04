from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    path(
        "cinema_halls/",
        cinema_hall_list,
        name="cinemahall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinemahall-detail"
    ),

    path("", include(router.urls)),
]

app_name = "cinema"
