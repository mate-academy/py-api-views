from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (MovieViewSet,
                          CinemaHallViewSet,
                          ActorList,
                          GenreList,
                          GenreDetail,
                          ActorDetail)

router = DefaultRouter()
router.register(r"movies", viewset=MovieViewSet)


cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})

cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [

    path("genres/", GenreList.as_view(), name="genre-list"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
