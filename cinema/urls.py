from django.urls import path

from cinema.views import movie_list, movie_detail, GenreList, GenreDetail, ActorList, ActorDetail

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genre/", GenreList.as_view(), name="genre-list"),  # Edited for APIView
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list"),  # GenericAPIView
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

]

app_name = "cinema"
