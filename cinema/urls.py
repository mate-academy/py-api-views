from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    MovieViewSet,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
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
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view(
        actions={"get": "list", "post": "create"}), name="cinema-hall-list",),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(
        actions={"get": "retrieve",
                 "put": "update",
                 "patch": "partial_update",
                 "delete": "destroy"}), name="cinema-hall-detail",),
]

app_name = "cinema"
