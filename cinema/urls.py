from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView

from cinema.views import MovieViewSet, CinemaHallViewSet, ActorListViewSet, ActorDetailViewSet, genre_list, genre_detail

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorListViewSet.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailViewSet.as_view(), name="actor-detail"),
    path("hall/", CinemaHallViewSet.as_view(actions={
        "get": "list",
        "post": "create",
    }), name="hall-list"),
    path("hall/<int:pk>/", CinemaHallViewSet.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }), name="hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
