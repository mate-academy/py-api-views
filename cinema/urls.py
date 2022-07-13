from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreList, GenreDetail, ActorListView, \
    ActorDetailView, CinemaHallListView, \
    CinemaHallDetailView, MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("cinema-halls/", CinemaHallListView.as_view(),
         name="cinema-hall-list"),
    path("cinema-halls/<int:pk>/", CinemaHallDetailView.as_view(),
         name="cinema-hall-detail"),

]

app_name = "cinema"
