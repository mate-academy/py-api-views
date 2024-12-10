from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie
from cinema.serializers import MovieSerializer
from cinema.views import MovieViewSet


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=200,
        )
        Movie.objects.create(
            title="Batman",
            description="Batman description",
            duration=190,
        )

    def test_movie_viewset_is_subclass_model_viewset(self):
        self.assertTrue(issubclass(MovieViewSet, ModelViewSet))

    def test_get_movies(self):
        movies = self.client.get("/api/cinema/movies/")
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(movies.status_code, status.HTTP_200_OK)
        self.assertEqual(movies.data, serializer.data)

    def test_post_movies(self):
        movies = self.client.post(
            "/api/cinema/movies/",
            {
                "title": "Superman",
                "description": "Superman description",
                "duration": 170,
            },
        )
        db_movies = Movie.objects.all()
        self.assertEqual(movies.status_code, status.HTTP_201_CREATED)
        self.assertEqual(db_movies.count(), 3)
        self.assertEqual(db_movies.filter(title="Superman").count(), 1)

    def test_post_invalid_movies(self):
        movies = self.client.post(
            "/api/cinema/movies/",
            {
                "title": "Superman",
                "description": "Superman description",
                "duration": "two hundred",
            },
        )
        superman_movies = Movie.objects.filter(title="Superman")
        self.assertEqual(movies.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(superman_movies.count(), 0)

    def test_get_movie(self):
        response = self.client.get("/api/cinema/movies/2/")
        serializer = MovieSerializer(
            Movie(
                id=2,
                title="Batman",
                description="Batman description",
                duration=190,
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_movie(self):
        response = self.client.get("/api/cinema/movies/100/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movie(self):
        self.client.put(
            "/api/cinema/movies/1/",
            {
                "title": "Watchman",
                "description": "Watchman description",
                "duration": 190,
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(
            [db_movie.title, db_movie.description, db_movie.duration],
            [
                "Watchman",
                "Watchman description",
                190,
            ],
        )
        self.assertEqual(db_movie.title, "Watchman")

    def test_put_invalid_movie(self):
        response = self.client.put(
            "/api/cinema/movies/1/",
            {
                "title": "Watchmen",
                "description": "Watchmen description",
                "duration": "fifty",
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_movie(self):
        response = self.client.patch(
            "/api/cinema/movies/1/",
            {
                "title": "Watchmen",
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.title, "Watchmen")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_movie(self):
        response = self.client.patch(
            "/api/cinema/movies/1/",
            {
                "duration": "fifty",
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie(self):
        response = self.client.delete(
            "/api/cinema/movies/1/",
        )
        db_movies_id_1 = Movie.objects.filter(id=1)
        self.assertEqual(db_movies_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_movie(self):
        response = self.client.delete(
            "/api/cinema/movies/1000/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
