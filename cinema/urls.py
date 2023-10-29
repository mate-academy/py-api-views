from django.urls import path
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    GenreDetail,
    GenreList,
    MovieViewSet,
)

cinema_hall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinemahall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinemahall-detail"
    ),
]

urlpatterns += router.urls

app_name = "cinema"
