from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("cinema_halls/", CinemaHallViewSet.as_view(
        actions={
            "get": "list",
            "post": "create"
        }
    ), name="hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
