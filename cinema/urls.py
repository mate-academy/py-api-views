from django.urls import path, include

from cinema.views import MovieViewList, GenreList, GenreDetail, ActorList, ActorDetail,CinemaHallList, CinemaHallDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewList)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("cinema_hole/", CinemaHallList.as_view(), name="cinema-hall-list"),
    path("cinema_hole/<int:pk>/", CinemaHallDetail.as_view(), name="cinema-hall-detail"),
]

app_name = "cinema"
