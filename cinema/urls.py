from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    ActorList,
    ActorDetail,
    GenreDetail,
    MovieViewSet,
    CinemaHallViewSet
)

cinemahall_list = CinemaHallViewSet.as_view(
    {
        "get": "list", "post": "create"
    }
)

cinemahall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update", "patch":
        "partial_update", "delete":
        "destroy"
    }
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinema_halls/", cinemahall_list, name="cinemahalls_list"),
    path(
        "cinema_halls/<int:pk>/", cinemahall_detail, name="cinemahalls_detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
