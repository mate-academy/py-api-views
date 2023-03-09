from django.urls import path, include
from rest_framework import routers
from cinema.views import MovieViewSet, CinemaHallViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("cinema-hall/", cinema_hall_list, name="cinema-hall"),
    path("cinema-hall/<int:pk>/", cinema_hall_detail, name="cinema-detail"),
]

app_name = "cinema"
