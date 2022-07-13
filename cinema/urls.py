from django.urls import path, include

from rest_framework import routers
from cinema.views import GenreList, GenreDetail, ActorList,\
    ActorDetail, CinemaHallViewSet, MovieViewSet


cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="exact-genre"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="exact-actor"),
    path("cinema_halls/", cinema_hall_list, name="cinema-halls-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail,
         name="exact-cinema-hall"),
    path("", include(router.urls))
]

app_name = "cinema"
