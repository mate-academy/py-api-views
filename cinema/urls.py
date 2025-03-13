from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("movies/genres/", GenreList.as_view(), name="genre-list"),
    path("movies/genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("movies/actors/", ActorList.as_view(), name="actor-list"),
    path("movies/actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "movies/cinemahalls/", CinemaHallList.as_view(), name="cinemahall-list"
    ),
    path(
        "movies/cinemahalls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinemahall-detail"
    ),
]

app_name = "cinema"
