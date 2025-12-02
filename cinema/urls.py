from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (MovieViewSet, CinemaHallViewSet,
                          GenreDetail,
                          ActorList, ActorDetail, GenreList)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
]

app_name = "cinema"
