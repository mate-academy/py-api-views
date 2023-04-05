from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorListGeneric,
    ActorDetailGeneric,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    MovieViewSet
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"}
    )

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls), name="movie"),
    path("actors/", ActorListGeneric.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailGeneric.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinema-halls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinema-halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
]

app_name = "cinema"
