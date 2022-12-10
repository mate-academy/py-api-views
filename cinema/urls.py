from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    genre_detail,
    genre_list,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_halls_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinema_halls_detail = CinemaHallViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
})

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_halls_list, name="cinema_halls-list"),
    path("cinema_halls/<int:pk>/", cinema_halls_detail, name="cinema_halls-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
