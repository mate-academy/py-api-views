from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    ActorList,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorDetail,
)
from rest_framework import routers

app_name = "cinema"
router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list", "post": "create"
    }
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
    path("actors/", ActorList.as_view(), name="actors"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),

]
