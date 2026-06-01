from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
)


router = DefaultRouter()
router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path(
        "cinema-halls/",
        cinema_hall_list,
        name="cinema-hall-list"
    ),
    path(
        "cinema-halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list-view"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail-view"
    ),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list-view"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail-view"
    ),
]

urlpatterns += router.urls

app_name = "cinema"
