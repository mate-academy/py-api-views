from django.urls import path, include
from rest_framework import routers

from cinema.views import (movie_list,
                          movie_detail,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet
                          )


CinemaHallList = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

CinemaHallDetail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # path("movies/", movie_list, name="movie-list"),
    # path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList, name="cinema_hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallDetail, name="cinema_hall-list"),
]

app_name = "cinema"
