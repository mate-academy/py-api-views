from django.urls import path, include
from rest_framework import routers
from cinema.views import GenreList, GenreDetail, ActorList, ActorDetail, CinemaHallSet, \
    MovieViewSet

cinema_hall_list = CinemaHallSet.as_view(actions={"get": "list", "post": "create"})

cinema_hall_detail = CinemaHallSet.as_view(
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
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("ciname_halls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinama_halls/", cinema_hall_list, name="cinema-hall-list"),

]

app_name = "cinema"
