from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView
)

router = routers.SimpleRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls), name="movies"),
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

]

app_name = "cinema"
