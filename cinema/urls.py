from django.urls import path

from cinema.views import movie_list, movie_detail, GenreLIst, GenreDetail

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genre/", GenreLIst.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view, name="genre-detail"),
]

app_name = "cinema"
