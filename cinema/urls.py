from django.urls import path, include
from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorDetail,
                          ActorList,
                          CinemaHallViewSet,
                          )
from rest_framework import routers


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
]

app_name = "cinema"
