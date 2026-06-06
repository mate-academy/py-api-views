from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),

    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),

    path("", include(router.urls)),
]
