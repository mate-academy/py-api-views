from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path(
        "api/cinema/genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "api/cinema/genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "api/cinema/actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "api/cinema/actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
]


app_name = "cinema"

router = DefaultRouter()
router.register(
    "api/cinema/cinema_halls",
    CinemaHallViewSet,
    basename="cinema-hall"
)
router.register(
    "api/cinema/movies",
    MovieViewSet,
    basename="movie"
)

urlpatterns += router.urls
