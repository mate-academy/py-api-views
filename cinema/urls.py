from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    GenreDetail,
    GenreList,
    MovieViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahalls/", cinemahall_list, name="cinemahall-list"),
    path(
        "cinemahalls/<int:pk>/",
        cinemahall_detail,
        name="cinemahall-detail"
    ),
]

app_name = "cinema"
