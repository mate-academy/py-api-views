from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema-halls-list"),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("cinema_halls/<int:pk>/", CinemaHallDetail.as_view(), name="cinema-halls-detail"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
]
