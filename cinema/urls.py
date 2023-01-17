from django.urls import path, include

from cinema.views import ActorList,\
    ActorDetail, \
    CinemaHallViewSet,\
    MovieViewSet,\
    GenreDetail,\
    GenreList
from rest_framework import routers
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})

hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("halls/", hall_list, name="cinema-hall-list"),
    path("halls/<int:pk>/", hall_detail, name="cinema-hall-list")
]

app_name = "cinema"
