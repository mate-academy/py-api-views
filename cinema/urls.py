from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorList, ActorDetail,
    GenreList, GenreDetail,
    CinemaHallViewSet, MovieViewSet
)


app_name = "cinema"

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("", include(router.urls)),
]
