from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list-create"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
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
]
