from django.urls import path, include
from rest_framework import routers
from cinema.views import (movie_list,
                          movie_detail,
                          MovieViewSet,
                          CinemaHallViewSet,
                          ActorList,
                          ActorDetail,
                          GenreList,
                          GenreDetail
                          )

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


urlpatterns = [
    path("", include(router.urls)),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("cinema_hall/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_hall/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"
    ),
    path("actor/", ActorList.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "cinema"
