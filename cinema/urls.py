from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list")
]

app_name = "cinema"
