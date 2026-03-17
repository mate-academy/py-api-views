from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),

    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),

    path("", include(router.urls)),
]

app_name = "cinema"
