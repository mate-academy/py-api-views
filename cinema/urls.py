from django.urls import path, include

from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

CINEMA_LIST = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})

CINEMA_DETAIL = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CINEMA_LIST,
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CINEMA_DETAIL,
        name="cinema-hall-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
