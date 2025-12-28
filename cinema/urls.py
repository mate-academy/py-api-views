from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})
router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", hall_list, name="hall-list"),
    path("cinema_halls/<int:pk>/", hall_detail, name="hall-detail"),
    path("", include(router.urls)),

]

app_name = "cinema"
