from django.urls import path, include
from rest_framework import routers

from cinema import views
from cinema.views import CinemaHallViewSet, MovieViewSet

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", views.GenreList.as_view()),
    path("genres/<int:pk>/", views.GenreDetail.as_view()),
    path("actors/", views.ActorList.as_view()),
    path("actors/<int:pk>/", views.ActorDetail.as_view()),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall-list"),
    path("cinema_halls/<int:pk>/",
         cinema_hall_detail, name="cinema_hall-detail"),
]

app_name = "cinema"
