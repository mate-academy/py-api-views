from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieSet,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("movies/", MovieSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListView.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genres-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
]

app_name = "cinema"
