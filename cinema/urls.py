from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, CinemaHallViewSet, GenreList, GenreDetail, ActorList, ActorDetail

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("cinemahalls/", CinemaHallViewSet.as_view(
        actions={
            "get": "list",
            "post": "create",
        }
    ), name="cinema-hall-list"),

    path("cinemahalls/<int:pk>/", CinemaHallViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }
    ), name="cinema-hall-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("genres/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
]

app_name = "station"

