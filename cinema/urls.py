from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GenreAPIView,
    GenreDetailAPIView,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_hall",
)
router.register(
    "movies",
    MovieViewSet,
    basename="movie",
)

urlpatterns = [
    # Genre
    path(
        "genres/",
        GenreAPIView.as_view(),
        name="genre-list",
    ),
    path(
        "genres/<int:pk>/",
        GenreDetailAPIView.as_view(),
        name="genre-detail",
    ),

    # Actor
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list",
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail",
    ),

    # CinemaHall + Movie через router
    path("", include(router.urls)),
]

app_name = "cinema"
