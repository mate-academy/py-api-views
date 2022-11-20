from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet, MovieViewSet
)

actor_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
actor_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve", "put": "update",
             "patch": "partial_update", "delete": "destroy"}
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),

    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    path("cinema_halls/", actor_list, name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", actor_detail, name="cinema-hall-detail"),
]

app_name = "cinema"
