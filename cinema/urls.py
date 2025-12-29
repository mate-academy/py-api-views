from django.urls import (
    path,
    include,
)
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})

cinema_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("", include(router.urls)),

    path("cinema_halls/", cinema_list),
    path("cinema_halls/<int:pk>/", cinema_detail),

    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),

    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
]
