from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView
)

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
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("halls/", cinema_hall_list, name="hall-list"),
    path("halls/<int:pk>/", cinema_hall_detail, name="hall-details")
]

app_name = "cinema"
