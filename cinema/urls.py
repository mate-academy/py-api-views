from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    MovieViewSet
)


router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
