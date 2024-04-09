from rest_framework import routers
from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("buses", MovieViewSet)

cinema_hall_list = (
    CinemaHallViewSet.as_view(
        actions={"get": "list", "post": "create"}
    )
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

app_name = "cinema"

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall_list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall_detail"
    ),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
]
