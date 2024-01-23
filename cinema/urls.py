from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList, ActorDetail
)

from rest_framework import routers


cinema_list = CinemaHallViewSet.as_view(actions={
            "get": "list",
            "post": "create",
        })
cinema_detail = CinemaHallViewSet.as_view(actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        })
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("cinema-halls/", cinema_list, name="cinema-halls-list"),
    path("cinema-halls/<pk>/", cinema_detail, name="cinema-halls-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<pk>/", ActorDetail.as_view(), name="actor-detail"),
]

app_name = "cinema"
