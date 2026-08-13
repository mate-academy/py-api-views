from django.urls import path, include

from .views import GenreAPIView, ActorListView, CinemaHallViewSet, MovieViewSet


app_name = "cinema"

urlpatterns = [
    path('actors/', ActorListView.as_view(), name='actor-list'),

    path('genres/', GenreAPIView.as_view(), name='genre-list'),

    path(
        'halls/',
        CinemaHallViewSet.as_view({'actions': ['list', 'create']}),
        name='hall-list'),
    path(
        'halls/<int:pk>/',
        CinemaHallViewSet.as_view({'actions': ['retrieve',
                                               'update',
                                               'partial_update']}),
        name='hall-detail'),

    path(
        'movies/',
        MovieViewSet.as_view({'actions': ['list', 'create']}),
        name='movie-list'),
    path(
        'movies/<int:pk>/',
        MovieViewSet.as_view({
            'actions': [
                'retrieve',
                'update',
                'partial_update',
                'destroy'
            ]
        }),
        name='movie-detail',
    ),
]
