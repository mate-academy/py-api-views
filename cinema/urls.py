from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view({"get": "list", "post": "create"}),
        name="cinema-hall-list",
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="cinema-hall-detail",
    ),
]

urlpatterns += router.urls

app_name = "cinema"
