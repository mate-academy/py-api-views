from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),

    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),

    path("cinemahalls/", cinemahall_list, name="cinemahall_list"),
    path("cinemahalls/<int:pk>/", cinemahall_detail, name="cinemahall_detail"),

    path("", include(router.urls))
]

app_name = "cinema"
