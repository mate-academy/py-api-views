from django.urls import path, include
from rest_framework import routers

from .views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
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
    path("genres/", GenreList.as_view(), name="genres"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinemahall_list, name="cinema_halls"),
    path("cinema_halls/<int:pk>/", cinemahall_detail,
         name="cinema_hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
