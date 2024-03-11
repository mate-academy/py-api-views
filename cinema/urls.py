from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreListView,
    GenreDetailView,
    ActorListView
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
]

app_name = "cinema"
