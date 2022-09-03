from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          MovieViewSet,
                          CinemaHallViewSet
                          )

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemaHallList = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinemaHallDetail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinemaHallList, name="cinemaHall-list"),
    path("cinema_halls/<int:pk>/", cinemaHallDetail, name="cinemaHall-detail"),
    path("", include(router.urls))

]

app_name = "cinema"
