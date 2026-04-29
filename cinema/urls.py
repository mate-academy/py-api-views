from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreListAPIView,
    GenreDetailAPIView,
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreListAPIView.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"
    ),
]

app_name = "cinema"
