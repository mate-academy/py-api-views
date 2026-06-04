from django.urls import path

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorView,
    GenreView,
)

urlpatterns = [
    path("movies/", CinemaViewSet.as_view(
        {}
    ), name="movie-list"),
    path("movies/<int:pk>/", CinemaViewSet.as_view(

    ), name="movie-detail"),
]

app_name = "cinema"
