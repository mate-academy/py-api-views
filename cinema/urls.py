from django.urls import path, include
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    MovieViewSet,
    CinemaHallViewSet,
)
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r"movies", MovieViewSet)

app_name = "cinema"

cinemahall_list = CinemaHallViewSet.as_view({"get": "list", "post": "create"})

cinemahall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
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
    path("", include(router.urls)),
]
