from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    GenreList,
    CinemaHallViewSet,
    ActorList,
    GenreDetail,
    ActorDetail,
)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
]

app_name = "cinema"
