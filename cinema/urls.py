from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreListView, GenreDetailView, ActorCreateListView, ActorDetailView, \
    CinemaHallViewSet, MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view(actions={"get": "retrieve",
                                                        "put": "update",
                                                        "patch": "partial_update",
                                                        "delete": "destroy"})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorCreateListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("halls/", cinema_hall_list, name="hall-list"),
    path("halls/<int:pk>/", cinema_hall_detail, name="hall-detail"),
]

app_name = "cinema"
