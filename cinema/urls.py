from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

routers = routers.DefaultRouter()

routers.register("cinema_halls", CinemaHallViewSet)
routers.register("movies", MovieViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors_detail"),
    path("genres/", GenreList.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres_detail")
] + routers.urls

app_name = "cinema"
