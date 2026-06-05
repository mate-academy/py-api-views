from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorList,
    GenreList,
    ActorDetail,
    GenreDetail,
)

router = DefaultRouter()

router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movies",
    MovieViewSet,
    basename="movies"
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre_detail"
         ),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/",
         ActorDetail.as_view(),
         name="actor_detail"
         ),
    path("", include(router.urls)),
]

app_name = "cinema"
