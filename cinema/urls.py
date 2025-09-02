from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList, GenreDetail, ActorDetail,
    ActorList, CinemaHallViewSet, MovieViewSet
)


cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})
cinema_hall_detail = CinemaHallViewSet.as_view({
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
    path("actors/", ActorList.as_view(), name="artist-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="artist-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
