from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("actors/", ActorList.as_view()),
]

app_name = "cinema"
