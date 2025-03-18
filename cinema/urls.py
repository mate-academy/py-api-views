from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (GenreView,
                          ActorView,
                          CinemaHallViewSet,
                          MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("genres/", GenreView.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreView.as_view(), name="genres-detail"),

    path("actors/", ActorView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorView.as_view(), name="actor-detail"),

    path("cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
]

app_name = "cinema"
