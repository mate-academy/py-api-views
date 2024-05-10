from django.urls import path, include
from rest_framework.routers import DefaultRouter
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

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("cinema_halls/", CinemaHallList.as_view()),
    path("cinema_halls/<int:pk>/", CinemaHallDetail.as_view()),
    path("", include(router.urls)),
]
