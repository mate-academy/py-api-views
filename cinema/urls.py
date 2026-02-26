from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet)


app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres_detail"),

    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),

    path("cinema_halls/",
         CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"}),
         name="cinema_hall_list"),
    path("cinema_halls/<int:pk>/",
         CinemaHallViewSet.as_view(actions={"get": "retrieve",
                                            "put": "update",
                                            "patch": "partial_update",
                                            "delete": "destroy"}),
         name="cinema_hall_detail"),

    path("", include(router.urls)),
]
