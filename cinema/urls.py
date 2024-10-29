from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CinemaHallViewSet,
    MovieViewSet, ActorList, GenreList, ActorDetail
)

app_name = "cinema"

router = DefaultRouter()
router.register(
    r"cinemahalls",
    CinemaHallViewSet,
    basename="cinemahall"
)
router.register(
    r"movies",
    MovieViewSet,
    basename="movie"
)


urlpatterns = [
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list-create"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "",
        include(router.urls)
    ),
]

urlpatterns += router.urls
