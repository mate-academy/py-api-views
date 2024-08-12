from django.urls import path, include
from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet
)
from rest_framework import routers
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_halls = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)
cinema_halls_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "patch": "partial_update",
        "put": "update",
        "delete": "destroy"
    }
)


urlpatterns = [
    path("", include(router.urls)),
    path("cinema_halls/",
         cinema_halls,
         name="cinema_halls"
         ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_halls_detail,
        name="cinema_halls-detail"
    ),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
]
