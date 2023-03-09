from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    MovieModelViewSet,
    CinemaHallViewSet,
    ActorListView,
    ActorDetailView, GenreListView, GenreDetailView
)

router = routers.DefaultRouter()
router.register("movies", MovieModelViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("cinema-hall/", cinema_hall_list, name="cinema-hall"),
    path("cinema-hall/<int:pk>/", cinema_hall_detail, name="cinema-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
]

app_name = "cinema"
