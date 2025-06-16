from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (CinemaHallViewSet,
                          MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail
                          )

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(r"movies", MovieViewSet, basename="movie")


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list-create"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
