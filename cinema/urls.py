from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    ActorDetail,
    ActorList,
    MovieViewSet,
    GenreDetail,
    GenreList,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
cinema_hall = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinema_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
urlpatterns = [
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("cinema_halls/", cinema_hall, name="cinema-hall_list"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema-hall_detail"),
] + router.urls

app_name = "cinema"
