# from django.urls import path, include
# from rest_framework import routers
# from cinema.views import GenreList, GenreDetail, ActorList, ActorDetail, CinemaHallViewSet, MovieViewSet
#
#
# router = routers.DefaultRouter()
# router.register("movie", MovieViewSet)
#
# cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
# cinema_hall_detail = CinemaHallViewSet.as_view(actions={
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy"
#         })
#
# urlpatterns = [
#     path("", include(router.urls)),
#     path("genre/", GenreList.as_view(), name="genre-list"),
#     path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
#     path("actor/", ActorList.as_view(), name="actor-list"),
#     path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
#     path("cinema_hall/", cinema_hall_list, name="cinema-hall-list"),
#     path("cinema_hall/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
# ]
#
# app_name = "cinema"

from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet
)

cinema_hall_list = CinemaHallViewSet.as_view({'get': 'list', 'post': 'create'})
cinema_hall_detail = CinemaHallViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_halls_list"),
    path("cinema_halls/<pk>/", cinema_hall_detail, name="cinema_halls_detail")

]

app_name = "cinema"
