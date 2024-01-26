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
    path("cinema_halls/", cinema_list, name="cinema-halls-list"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema-halls-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
] + router.urls

app_name = "cinema"
