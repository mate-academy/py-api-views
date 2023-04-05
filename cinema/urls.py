from django.urls import path

from cinema.views import (
    MovieList,
    MovieDetail,
    GenreList,
    GenreDetail,
    CinemaHallList,
    CinemaHallDetail,
    ActorList,
    ActorDetail
)

urlpatterns = [
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallDetail.as_view(), name="hall-detail"),
]

app_name = "cinema"
