from django.urls import path, include
from rest_framework import routers

from cinema.views import (
     CinemaHallViewSet,
     MovieViewSet,
     GenreList,
     GenreDetail,
     ActorList,
     ActorDetail
 )

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="actor-detail"),
    path("actors/", ActorList.as_view(), name="genre-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
