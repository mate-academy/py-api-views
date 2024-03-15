from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallDetail,
    CinemaHallList,
    GenreDetail,
    GenreList,
    MovieViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahalls/", CinemaHallList.as_view(), name="cinemahall-list"),
    path(
        "cinemahalls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinemahall-detail"
    ),
]

app_name = "cinema"
