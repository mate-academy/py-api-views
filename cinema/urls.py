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
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
                  path("genres/", GenreList.as_view(), name="genre-list"),
                  path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
                  path("actors/", ActorList.as_view(), name="actor-list"),
                  path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

              ] + router.urls

app_name = "cinema"
