from django.urls import path, include

from rest_framework import routers

from .views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halsl", CinemaHallViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pl>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
