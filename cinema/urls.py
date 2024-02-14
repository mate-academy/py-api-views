from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, genre_list, genre_detail, ActorList, ActorDetail, CinemaHallView

router = routers.DefaultRouter()

movie_list = router.register(r'movies', MovieViewSet, basename='movies')

cinema_hall_list = CinemaHallView.as_view({"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallView.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahalls/", cinema_hall_list, name="cimemahall-list"),
    path("cinemahalls/<int:pk>/", cinema_hall_detail, name="cimemahall-detail"),


]
app_name = "cinema"
