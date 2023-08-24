from django.urls import path, include

from rest_framework import routers
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MoviesViewSet
)

router = routers.DefaultRouter()
router.register("movies", MoviesViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema_halls-list"),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema_halls-detail"
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
