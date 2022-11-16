from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreDetailView,
    GenreListView,
    ActorListView,
    ActorDetailView,
    CinemaHallViewSet,
)

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
cinema_halls_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path(
        "actors/",
        ActorListView.as_view(),
        name="actor-hall-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetailView.as_view(),
        name="actor-hall-detail"
    ),
    path(
        "cinema-halls/",
        cinema_halls_list,
        name="cinema-hall-list"
    ),
    path(
        "cinema-halls/<int:pk>/",
        cinema_halls_detail,
        name="cinema-hall-detail"
    ),
]

app_name = "cinema"
