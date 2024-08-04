from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorDetail,
    ActorList,
)

app_name = "cinema"

cinema_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

cinema_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movies")


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("cinema_halls/", cinema_list, name="cinema-list"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema-detail"),
]
