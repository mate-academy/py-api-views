from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    GenreList,
    GenreDetail,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)


router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
