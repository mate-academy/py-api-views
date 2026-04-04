from django.contrib.admin import actions
from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    # path("movies/", movie_list, name="movie-list"),
    # path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"}),
        name="cinema_hall",
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="cinema_hall_detail",
    ),
    # path("cinema_halls/", cinema_hall_list, name="cinema_hall_list"),
    # path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema_hall_detail"),
    path("movies/", include(router.urls)),
]

app_name = "cinema"
