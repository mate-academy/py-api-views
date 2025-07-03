from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema import views
from cinema.views import GenreList, GenreDetail, ActorViewSet, CinemaHallViewSet, ScreeningViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'screenings', ScreeningViewSet, basename='screening')

actor_list = ActorViewSet.as_view({'get': 'list', 'post': 'create'})
actor_detail = ActorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
cinema_list = CinemaHallViewSet.as_view({'get': 'list', 'post': 'create'})
cinema_detail = CinemaHallViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
urlpatterns = [
    path('', include(router.urls)),

    # Genres (APIView)
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),

    # Actors (ViewSet)
    path('actors/', actor_list, name='actor-list'),
    path('actors/<int:pk>/', actor_detail, name='actor-detail'),

    # CinemaHalls (ViewSet)
    path('cinemas/', cinema_list, name='cinema-list'),
    path('cinemas/<int:pk>/', cinema_detail, name='cinema-detail'),
]


app_name = "cinema"
