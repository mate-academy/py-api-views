from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    ActorListCreateView,
    ActorRetrieveUpdateDestroyView,
    GenreAPIView,
    GenreDetailAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("actors/", ActorListCreateView.as_view(), name="actor-list-create"),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail",
    ),
    path("genres/", GenreAPIView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/",
         GenreDetailAPIView.as_view(),
         name="genre-detail"
         ),
    path("", include(router.urls)),
]
