from django.urls import path, include
from cinema.views import (GenreList, GenreDetail, ActorList,
                          ActorDetail, CinemaHallViewSet, MovieViewSet)
from rest_framework.routers import DefaultRouter

router_cinema_halls = DefaultRouter()
router_cinema_halls.register("cinema_halls", CinemaHallViewSet)
router_movies = DefaultRouter()
router_movies.register("movies", MovieViewSet)

urlpatterns = [
    # path("movies/", movie_list, name="movie-list"),
    # path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router_cinema_halls.urls)),
    path("", include(router_movies.urls))
]

app_name = "cinema"
