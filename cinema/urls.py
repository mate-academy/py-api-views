from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    movie_list,
    movie_detail,
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
)

app_name = "cinema"
router = routers.DefaultRouter()

router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("", include(router.urls)),
]
