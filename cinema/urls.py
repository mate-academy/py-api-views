from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movie", MovieViewSet)

urlpatterns = [
    path("genre/",
         GenreList.as_view(),
         name="genre-list"),
    path("genre/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("actor/", ActorList.as_view(),
         name="actor-list"),
    path("actor/<int:pk>/",
         GenreDetail.as_view(),
         name="actor-detail"),
    path("cinemahall/",
         CinemaHallList.as_view(),
         name="actor-list"),
    path("cinemahall/<int:pk>/",
         CinemaHallDetail.as_view(),
         name="actor-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
