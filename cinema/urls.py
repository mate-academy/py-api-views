from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    MovieViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            actions={"get": "list", "post": "create"}
        ),
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="cinema-hall-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
