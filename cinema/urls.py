from django.urls import path, include
from rest_framework import routers

from cinema import views

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movies")

cinema_hall_list = views.CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinema_hall_detail = views.CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", views.GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        views.GenreDetail.as_view(),
        name="genre-detail"
    ),
    path("actors/", views.ActorList.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        views.ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinema_halls/",
        cinema_hall_list,
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
]

app_name = "cinema"
