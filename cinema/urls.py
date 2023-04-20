from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

cinema_hall_list = CinemaHallViewSet.as_view(actions={
    "get": "list", "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("", include(router.urls)),
    path("genres", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_hall/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_hall/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),

]

app_name = "cinema"
