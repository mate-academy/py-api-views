from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from cinema.serializers import MovieSerializer
from cinema.models import Movie, Actor, Genre
from cinema.views import MovieViewSet
from rest_framework.viewsets import ModelViewSet


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создаём объекты, нужные для ManyToMany (актеры и жанры)
        self.actor = Actor.objects.create(first_name="Tom", last_name="Cruise")
        self.genre = Genre.objects.create(name="Drama")

        self.movie1 = Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=200,
        )
        self.movie1.actors.add(self.actor)
        self.movie1.genres.add(self.genre)

        self.movie2 = Movie.objects.create(
            title="Batman",
            description="Batman description",
            duration=190,
        )
        self.movie2.actors.add(self.actor)
        self.movie2.genres.add(self.genre)

    def test_movie_viewset_is_subclass_model_viewset(self):
        self.assertTrue(issubclass(MovieViewSet, ModelViewSet))

    def test_get_movies(self):
        movies = self.client.get("/api/cinema/movies/")
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(movies.status_code, status.HTTP_200_OK)
        self.assertEqual(movies.data, serializer.data)

    def test_post_movies(self):
        data = {
            "title": "Superman",
            "description": "Superman description",
            "duration": 170,
            "actors": [self.actor.id],
            "genres": [self.genre.id]
        }
        response = self.client.post("/api/cinema/movies/", data, format="json")
        db_movies = Movie.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(db_movies.count(), 3)
        self.assertEqual(db_movies.filter(title="Superman").count(), 1)

    def test_post_invalid_movies(self):
        data = {
            "title": "Superman",
            "description": "Superman description",
            "duration": "two hundred",
            "actors": [self.actor.id],
            "genres": [self.genre.id]
        }
        response = self.client.post("/api/cinema/movies/", data, format="json")
        superman_movies = Movie.objects.filter(title="Superman")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(superman_movies.count(), 0)

    def test_get_movie(self):
        response = self.client.get(f"/api/cinema/movies/{self.movie2.id}/")
        serializer = MovieSerializer(self.movie2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_movie(self):
        response = self.client.get("/api/cinema/movies/100/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movie(self):
        data = {
            "title": "Watchman",
            "description": "Watchman description",
            "duration": 190,
            "actors": [self.actor.id],
            "genres": [self.genre.id]
        }
        response = self.client.put("/api/cinema/movies/1/", data, format="json")
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(
            [db_movie.title, db_movie.description, db_movie.duration],
            [
                "Watchman",
                "Watchman description",
                190,
            ],
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_movie(self):
        data = {
            "title": "Watchmen",
            "description": "Watchmen description",
            "duration": "fifty",
            "actors": [self.actor.id],
            "genres": [self.genre.id]
        }
        response = self.client.put("/api/cinema/movies/1/", data, format="json")
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_movie(self):
        response = self.client.patch(
            "/api/cinema/movies/1/",
            {"title": "Watchmen"},
            format="json"
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.title, "Watchmen")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_movie(self):
        response = self.client.patch(
            "/api/cinema/movies/1/",
            {"duration": "fifty"},
            format="json"
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie(self):
        response = self.client.delete("/api/cinema/movies/1/")
        db_movies_id_1 = Movie.objects.filter(id=1)
        self.assertEqual(db_movies_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_movie(self):
        response = self.client.delete("/api/cinema/movies/1000/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

