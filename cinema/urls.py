from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorsList,
    ActorsDetail,
    CinemaViewSet,
    MoviesViewSet,
)

cinema_hall_list = CinemaViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()
router.register("movies", MoviesViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorsList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorsDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema-halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
