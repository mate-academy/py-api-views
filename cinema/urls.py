from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MoviesViewSet
)

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinema_halls_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = routers.DefaultRouter()
router.register("movies", MoviesViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("cinema_halls/", cinema_halls_list, name="cinema_halls-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_halls_detail,
        name="cinema_halls-detail"
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
