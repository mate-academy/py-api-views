from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorDetailView,
    ActorListCreateView,
    CinemaHallViewSet,
    GenreDetailView,
    GenreListCreateView,
    MovieViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreListCreateView.as_view()),
    path("genres/<int:pk>/", GenreDetailView.as_view()),
    path("actors/", ActorListCreateView.as_view()),
    path("actors/<int:pk>/", ActorDetailView.as_view()),
    path(
        "cinema-halls/",
        CinemaHallViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "cinema-halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("", include(router.urls)),
]
