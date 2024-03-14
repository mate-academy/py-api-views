from django.urls import path, include

from cinema.views import (
    GenreDetail,
    GenreList,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


cinema_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

cinema_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahalls/", cinema_list, name="cinema-hall-list"),
    path("cinemahalls/<int:pk>/", cinema_detail, name="cinema-hall-detail"),
    path("", include(router.urls)),
]


app_name = "cinema"
