from django.urls import (
    path,
    include
)
from rest_framework import routers

from cinema.views import (
    GenerList,
    GenerDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("geners/", GenerList.as_view(), name="gener-list"),
    path("geners/<int:pk>/", GenerDetail.as_view(), name="gener-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema_hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema_hall-detail"
    ),
]

app_name = "cinema"
