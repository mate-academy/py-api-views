from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorListView,
    ActorDetailView,
    CinemaListView,
    CinemaDetailView,
    GenreListView,
    GenreDetailView,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("actors/", ActorListView.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actors-detail"),
    path("genres/", GenreListView.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genres-detail"),
    path("cinemas/", CinemaListView.as_view(), name="cinemas-list"),
    path("cinemas/<int:pk>/", CinemaDetailView.as_view(), name="cinemas-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
