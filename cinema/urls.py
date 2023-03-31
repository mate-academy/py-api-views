from django.urls import path, include
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
cinemahall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinemahall_list, name="cinemahall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinemahall_detail,
        name="cinemahall-detail"
    ),
    path("cinema/actors/", ActorList.as_view(), name="actors-list"),
    path(
        "cinema/actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actors-detail"
    )] + router.urls

app_name = "cinema"
