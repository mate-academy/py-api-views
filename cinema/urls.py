from django.urls import path, include

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet)
from rest_framework import routers


cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
    "patch": "partial_update",
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahall/", cinema_hall_list, name="cinema-hall-list"),
    path("cinemehall/<int:pk>/",
         cinema_hall_detail,
         name="cinema-hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
