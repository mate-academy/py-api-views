from django.urls import path

from cinema.views import GenreList, GenreDetail

urlpatterns = [
    path("movies/", GenreList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", GenreDetail.as_view(), name="movie-detail"),
]

app_name = "cinema"
