from django.urls import path

from cinema.views import (
    MovieList, MovieDetail,
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallList, CinemaHallDetail,
)

app_name = "cinema"

urlpatterns = [
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", CinemaHallList.as_view(), name="cinema-hall-list"),
    path("cinema-halls/<int:pk>/", CinemaHallDetail.as_view(), "cinema-hall-detail"),
]
