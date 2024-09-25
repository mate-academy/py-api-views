from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreAPIView,
    ActorListCreateView,
    ActorRetrieveUpdateDestroyView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

app_name = "cinema"

cinema_hall_list = CinemaHallViewSet.as_view({"get": "list", "post": "post"})

cinema_hall_detail = CinemaHallViewSet.as_view(
    {"get": "retrieve", "put": "put", "patch": "patch", "delete": "destroy"}
)

urlpatterns = [
    path("cinema/genres/", GenreAPIView.as_view(), name="genre-list-create"),
    path(
        "cinema/genres/<int:pk>/",
        GenreAPIView.as_view(),
        name="genre-detail"
    ),
    path(
        "cinema/actors/",
        ActorListCreateView.as_view(),
        name="actor-list-create"),
    path(
        "cinema/actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail",
    ),
    path(
        "cinema/cinema_halls/",
        cinema_hall_list,
        name="cinema_hall-list-create"
    ),
    path(
        "cinema/cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall-detail"
    ),
    path("api/", include(router.urls)),
]
