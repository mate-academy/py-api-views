
from django.urls import path, include

from .views import  MovieViewSet, ActorList, ActorDetail, GenreDetail, CinemaHallViewSet, \
    GenreList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name='actor-list'),
    path("actors/<int:pk>/", ActorDetail.as_view(), name='actor-detail'),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(actions={
        'delete': 'destroy', 'put': 'update', 'patch': 'partial_update', 'get': 'retrieve'}), name='cinema-detail'),
    path('cinema_halls/', CinemaHallViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path("", include(router.urls)),
]

app_name = "cinema"
