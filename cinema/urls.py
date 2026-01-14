from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView,
    CinemaHallViewSet
)

router = routers.SimpleRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreListView.as_view(), name="genres"),
    path(
        "genres/<int:pk>/",
        GenreDetailView.as_view(),
        name="genres_detail"
    ),
    path(
        "actors/",
        ActorListView.as_view(),
        name="actor_list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetailView.as_view(),
        name="actor_detail"
    ),
    path(
        "cinema-halls/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "list",
                "post": "create"
            }
        ),
        name="cinema_hall_list"
    ),
    path(
        "cinema-halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "patch": "partial_update",
                "put": "update",
                "delete": "destroy"
            }
        ),
        name="cinema_hall_detail"
    ),

    path("", include(router.urls), name="movies"),

]

app_name = "cinema"
