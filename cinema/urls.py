from django.urls import path
from cinema import views

app_name = "cinema"

urlpatterns = [
    path("genres/", views.GenreListCreateView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", views.GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", views.ActorListCreateView.as_view(), name="actor-list-create"),
    path("actors/<int:pk>/", views.ActorDetailView.as_view(), name="actor-detail"),
    path("cinema-halls/", views.CinemaHallListCreateView.as_view(), name="cinema-hall-list-create"),
    path("cinema-halls/<int:pk>/", views.CinemaHallDetailView.as_view(), name="cinema-hall-detail"),
    path("movies/", views.MovieListCreateView.as_view(), name="movie-list-create"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
]
