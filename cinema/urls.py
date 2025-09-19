from django.urls import path, include

from rest_framework import routers
from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]
