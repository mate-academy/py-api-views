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

cinema_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("cinema_halls/", cinema_list, name="cinema-list"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
