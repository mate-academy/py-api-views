from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)


CinemaHall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
CinemaHall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHall_list, name="cinema_hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHall_detail,
        name="cinema_hall-detail"
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
