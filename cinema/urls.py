from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet, MovieViewSet
)

# 1. Створюємо роутер для ViewSets (CinemaHall та Movie)
router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    # 2. Маршрути для Genre (APIView)
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # 3. Маршрути для Actor (GenericAPIView)
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # 4. Підключаємо роутер (це додасть маршрути для movies/ та cinema_halls/)
    path("", include(router.urls)),
]

app_name = "cinema"
