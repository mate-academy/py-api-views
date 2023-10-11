from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallView,
    MovieView,
    GenreView,
    ActorListView,
    ActorDetailView,
)

halls_list = CinemaHallView.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

halls_detail = CinemaHallView.as_view(
    actions={
        "get": "retrieve",
        "post": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
router = routers.DefaultRouter()
router.register("movies", MovieView)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("halls/", halls_list, name="halls-list"),
    path("halls/<int:pk>/", halls_detail, name="halls-detail"),
]

app_name = "cinema"
