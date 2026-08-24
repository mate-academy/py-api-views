from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
)

app_name = "cinema"
router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("", include(router.urls)),
]
