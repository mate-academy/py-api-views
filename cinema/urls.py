from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({"get": "retrieve",
                                                "put": "update",
                                                "patch": "partial_update",
                                                "delete": "destroy"})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/",
         GenreList.as_view(),
         name="genre-list"),
    path("genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("actors/",
         ActorList.as_view(),
         name="actor-list"),
    path("actors/<int:pk>/",
         ActorDetail.as_view(),
         name="actor-detail"),
]

app_name = "cinema"
