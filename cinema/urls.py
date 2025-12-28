from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    GenreDetail,
    GenreList,
    MovieViewSet, CinemaHallViewSet)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

]

app_name = "cinema"
