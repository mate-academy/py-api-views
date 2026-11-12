from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    genre_list,
    genre_detail,
    MovieViewSet
)


router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", CinemaHallList.as_view(), name="cinema-hall-list"),

    path(
        "cinema-halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema-hall-detail"
    ),

    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
