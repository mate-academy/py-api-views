from os import name

from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorList, ActorDetail,
    GenreList, GenreDetail
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path(
        "actors/",
        ActorList.as_view(),
        name="actor_list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor_detail"
    ),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre_list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(), name="genre_detail"
    ),


    path(
        "",
        include(router.urls)
    ),




]

app_name = "cinema"
