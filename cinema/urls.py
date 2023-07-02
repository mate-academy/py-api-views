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
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
] + router.urls

app_name = "cinema"
