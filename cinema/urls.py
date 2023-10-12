from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    MovieViewSet,
    CinemaHallViewSet,
)

cinema_hall_detail_view = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
        "patch": "partial_update",
    }
)
cinema_hall_list_view = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_hall_list_view, name="hall-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail_view, name="hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
