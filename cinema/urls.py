from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet)


cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("cinema/genres/", GenreList.as_view()),
    path("cinema/genres/<int:pk>/", GenreDetail.as_view()),
    path("cinema/actors/", ActorList.as_view()),
    path("cinema/actors/<int:pk>/", ActorDetail.as_view()),
    path("cinema/cinema_halls/", cinema_hall_list),
    path("cinema/cinema_halls/<int:pk>/", cinema_hall_detail),
    path("cinema/", include(router.urls)),
]

app_name = "cinema"
