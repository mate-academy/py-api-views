from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    GenreListView,
    GenreDetailView,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path(
        "hall/",
        CinemaHallList.as_view(actions={"get": "list", "post": "create"}),
        name="hall-list",
    ),
    path(
        "hall/<int:pk>/",
        CinemaHallDetail.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="hall-detail",
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
