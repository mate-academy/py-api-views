from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    genre_list,
    genre_detail,
    ActorList,
    ActorDetail,
    MovieViewSet,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahalls")
urlpatterns = [
    path("", include(routers.urls)),
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

]

app_name = "cinema"
