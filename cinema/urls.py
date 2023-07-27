from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreDetail,
    GenreList,
    ActorDetail,
    ActorList,
    MovieViewSet,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")


urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(),
         name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(),
         name="actor-detail"),
    path("genres/", GenreList.as_view(),
         name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(),
         name="genre-detail"),
]

app_name = "cinema"
