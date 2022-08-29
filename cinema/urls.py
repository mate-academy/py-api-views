from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    MovieViewSet,
)

cinemaHall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinemaHall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("cinema_halls/", cinemaHall_list, name="cinema-halls-list"),
    path("cinema_halls/<int:pk>/", cinemaHall_detail, name="cinema-halls-detail"),
]

app_name = "cinema"
