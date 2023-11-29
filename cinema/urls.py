from django.urls import path

from cinema.views import GenreList

urlpatterns = [
    path("movies/", GenreList.as_view(), name="movie-list"),
    # path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
