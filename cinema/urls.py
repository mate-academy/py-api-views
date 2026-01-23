from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView, GenreDetailAPIView,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register(r'cinema/actors', ActorViewSet, basename='actor') # ActorViewSet usa o router
router.register(r'cinema/cinema_halls', CinemaHallViewSet, basename='cinemahall') # CinemaHallViewSet usa o router
router.register(r'cinema/movies', MovieViewSet, basename='movie') # MovieViewSet usa o router

urlpatterns = [
    # Rotas manuais para APIView (Genre)
    path('cinema/genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('cinema/genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),

    # Rotas automáticas do Router
    path('cinema/', include(router.urls)),
]
