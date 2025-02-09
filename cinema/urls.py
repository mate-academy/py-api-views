from django.urls import path, include
from rest_framework import routers

from cinema import views


app_name = "cinema"

cinema_hall_list = views.CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})

cinema_hall_detail = views.CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "genres/",
        views.GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        views.GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        views.ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        views.ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinemahalls/",
        cinema_hall_list,
        name="cinemahall-list"
    ),
    path(
        "cinemahalls/<int:pk>/",
        cinema_hall_detail,
        name="cinemahall-detail"
    )
]
