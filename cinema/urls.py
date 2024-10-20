from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)

app_name = "cinema"
router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahall")


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/create/", GenreList.as_view(), name="genre-create"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path(
        "genres/<int:pk>/update/",
        GenreDetail.as_view(),
        name="genre-update"
    ),
    path(
        "genres/<int:pk>/delete/",
        GenreDetail.as_view(),
        name="genre-delete"
    ),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
]
