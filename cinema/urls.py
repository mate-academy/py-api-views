from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (CinemaHallViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          MovieViewSet
                          )

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


router_movies = DefaultRouter()
router_movies.register(r"movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_halls_list, name="cinema-halls-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema-hall"),
    path("", include(router_movies.urls))
]

app_name = "cinema"
