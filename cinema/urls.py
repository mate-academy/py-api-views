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

app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", CinemaHallList.as_view(), name="cinema-hall-list"),
    path(
        "cinema-halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema-hall-detail"
    ),
    path("", include(router.urls))
]
