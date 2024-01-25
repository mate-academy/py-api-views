from django.urls import path

from cinema.views import movie_list, movie_detail, GenreList, GenreDetail, ActorList, ActorDetail, CinemaHallViewSet

cinema_hall_list = CinemaHallViewSet.as_view({"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy", })


urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genre/", GenreList.as_view(), name="genre-list"),  # Edited for APIView
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list"),  # GenericAPIView
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_hall/", cinema_hall_list, name="cinema-hall-list"),
    path("cinema_hall/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
]

app_name = "cinema"
