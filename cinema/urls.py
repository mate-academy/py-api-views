from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreAPIView, GenreDetailAPIView, ActorAPIView, ActorDetailAPIView, CinemaHallViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'cinema/cinema_halls', CinemaHallViewSet, basename='cinemahall')
router.register(r'cinema/movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('cinema/genres/', GenreAPIView.as_view(), name='genre-list'),
    path('cinema/genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('cinema/actors/', ActorAPIView.as_view(), name='actor-list'),
    path('cinema/actors/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),
    path('', include(router.urls)),
]

app_name = 'cinema'
