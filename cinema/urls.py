from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (CinemaHallViewSet,
                          MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail)

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


router_movies = DefaultRouter()
router_movies.register(r"movies", MovieViewSet)

urlpatterns = [
    path(
        "api/cinema/genres/",
        GenreList.as_view(),
        name="genres-list"
    ),
    path(
        "api/cinema/genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail",
    ),
    path(
        "api/cinema/actors/",
        ActorList.as_view(),
        name="actors-list"
    ),
    path(
        "api/cinema/actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "api/cinema/cinema_halls/",
        cinema_halls_list,
        name="cinema-halls-list"
    ),
    path(
        "api/cinema/cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall"
    ),
    path("api/cinema/", include(router_movies.urls))
]

app_name = "cinema"
