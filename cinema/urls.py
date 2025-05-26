from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet, MovieViewSet
)

app_name = "cinema"
router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("", include(router.urls)),
]
