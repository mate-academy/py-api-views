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

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


cinema_hall_list_view = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_hall_detail_view = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("cinema-halls/", cinema_hall_list_view, name="cinema-hall-list"),
    path("cinema-halls/<int:pk>/", cinema_hall_detail_view, name="cinema-hall-detail"),

]

app_name = "cinema"
