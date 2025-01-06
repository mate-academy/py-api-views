from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          ActorList,
                          ActorDetail,
                          GenreList,
                          CinemaHallViewSet,
                          GenreDetail)


movie_router = routers.DefaultRouter()
movie_router.register(r"movies", MovieViewSet, basename="movie")

cinema_hall_list = CinemaHallViewSet.as_view(
    {
        "get": "list",
        "post": "create"
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path(
        "", include(movie_router.urls)
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail",
    ),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "cinema_halls/",
        cinema_hall_list,
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),

]

app_name = "cinema"
