from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    MovieViewSet,
    CinemaHallViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
]
