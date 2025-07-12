from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = DefaultRouter()

router.register(r"movies", MovieViewSet, basename="movie")

cinema_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})

cinema_detail = CinemaHallViewSet.as_view(actions={"get": "retrieve",
                                                   "put": "update",
                                                   "patch": "partial_update",
                                                   "delete": "destroy"
                                                   })



urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_list, name="cinema-hall"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema-detail"),
    path("", include(router.urls)),

]
