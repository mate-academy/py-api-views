from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet, CinemaHallViewSet, ActorList,
                          ActorDetail, GenreDetail, GenreList)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_halls = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("cinema_halls/", cinema_halls),
    path("cinema_halls/<int:pk>/", cinema_hall_detail),
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
]

app_name = "cinema"
