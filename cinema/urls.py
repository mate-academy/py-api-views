from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    movie_detail,
    movie_list,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("", include(router.urls)),
]

app_name = "cinema"
