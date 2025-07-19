from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreList,
    MovieViewSet,
    GenreDetail,
    ActorDetail,
    ActorList
)

cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
    "patch": "partial_update"
})
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("cinema_halls/", cinema_hall_list, name="cinema_list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema_detail"),
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres_detail"),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors_detail"),
]

app_name = "cinema"
