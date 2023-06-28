from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    ActorList,
    ActorDetail
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)


hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "name"})
hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "putch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("halls/", hall_list, name="hall-list"),
    path("halls/<int:pk>/", hall_detail, name="hall-detail"),
]

app_name = "cinema"
