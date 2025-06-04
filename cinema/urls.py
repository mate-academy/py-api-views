from django.urls import path, include
from rest_framework.generics import GenericAPIView
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"
router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movies")
urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-api"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("", include(router.urls)),
]
