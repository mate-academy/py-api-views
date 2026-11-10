from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cinema.views import (ActorDetail,
                          ActorList,
                          CinemaHallViewSet,
                          GenreDetail,
                          GenreList,
                          MovieViewSet
                          )


router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view({"get": "list",
                                                     "post": "create", }),
         name="cinema_hall_list",
         ),
    path("cinema_halls/<int:pk>/",
         CinemaHallViewSet.as_view({"get": "retrieve",
                                    "put": "update",
                                    "patch": "partial_update",
                                    "delete": "destroy",
                                    }),
         name="cinema_hall_detail",
         ),
    path("", include(router.urls)),
]
app_name = "cinema"
