
from django.urls import path
from cinema.views import (GenreList, GenreDetail,
                          ActorList, ActorDetail,
                          CinemaHallList, CinemaHallDetail,
                          MovieViewSet)
movie_list = MovieViewSet.as_view(
    actions={"get": "list",
             "post": "create"},
)
movie_detail = MovieViewSet.as_view(
    actions={"get": "retrieve",
             "put": "update",
             "patch": "partial_update",
             "delete": "destroy"},
)
urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema_hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallDetail.as_view(),
         name="cinema_hall-detail"),
]
app_name = "cinema"
