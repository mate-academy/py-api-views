from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet, ActorList,
                          ActorDetail, GenreList,
                          GenreDetail, CinemaHallViewSet)

cinema_list = CinemaHallViewSet.as_view(actions={"get": "list",
                                                 "post": "create"}
                                        )
cinema_detail = CinemaHallViewSet.as_view(actions={"get": "retrieve",
                                                   "put": "update",
                                                   "delete": "destroy",
                                                   "patch": "partial_update"}
                                          )

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls), name="movies"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("cinema_halls/", cinema_list, name="cinema_hall_list"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema_hall_detail"),
]

app_name = "cinema"
