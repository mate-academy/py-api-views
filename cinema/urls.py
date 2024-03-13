from django.urls import path

from cinema.views import MovieList, MovieDetail

urlpatterns = [
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]

app_name = "cinema"
