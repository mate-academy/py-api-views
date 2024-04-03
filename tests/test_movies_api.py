from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from cinema.models import Movie, Actor, Genre


class MovieAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            "title": "Test Movie",
            "description": "Test Description",
            "duration": 120,
        }
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.genre = Genre.objects.create(name="Action")

    def test_create_movie(self):
        response = self.client.post(
            "/api/cinema/movies/", self.movie_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)

    def test_retrieve_movie(self):
        movie = Movie.objects.create(
            title="Test Movie", description="Test Description", duration=120
        )
        response = self.client.get(f"/api/cinema/movies/{movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_movie(self):
        movie = Movie.objects.create(
            title="Test Movie", description="Test Description", duration=120
        )
        updated_data = {
            "title": "Updated Movie",
            "description": "Updated description",
            "duration": 360,
        }
        response = self.client.put(
            f"/api/cinema/movies/{movie.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie.refresh_from_db()
        self.assertEqual(movie.__dict__, {**movie.__dict__, **updated_data})

    def test_partial_update_movie(self):
        movie = Movie.objects.create(
            title="Test Movie", description="Test Description", duration=120
        )
        updated_data = {"title": "Updated Movie"}
        response = self.client.patch(
            f"/api/cinema/movies/{movie.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie.refresh_from_db()
        self.assertEqual(movie.title, "Updated Movie")

    def test_delete_movie(self):
        movie = Movie.objects.create(
            title="Test Movie", description="Test Description", duration=120
        )
        response = self.client.delete(f"/api/cinema/movies/{movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)


class ActorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_actor(self):
        actor_data = {"first_name": "John", "last_name": "Doe"}
        response = self.client.post(
            "/api/cinema/actors/", actor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 1)

    def test_retrieve_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        response = self.client.get(f"/api/cinema/actors/{actor.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        updated_data = {"first_name": "Jane", "last_name": "Smith"}
        response = self.client.put(
            f"/api/cinema/actors/{actor.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actor.refresh_from_db()
        self.assertEqual(actor.first_name, "Jane")
        self.assertEqual(actor.last_name, "Smith")

    def test_partial_update_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        updated_data = {"first_name": "Jane"}
        response = self.client.patch(
            f"/api/cinema/actors/{actor.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actor.refresh_from_db()
        self.assertEqual(actor.first_name, "Jane")

    def test_delete_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        response = self.client.delete(f"/api/cinema/actors/{actor.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Actor.objects.count(), 0)


class GenreAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_genre(self):
        genre_data = {"name": "Action"}
        response = self.client.post(
            "/api/cinema/genres/", genre_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_genre(self):
        genre = Genre.objects.create(name="Action")
        response = self.client.get(f"/api/cinema/genres/{genre.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_genre(self):
        genre = Genre.objects.create(name="Action")
        updated_data = {"name": "Thriller"}
        response = self.client.put(
            f"/api/cinema/genres/{genre.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        genre.refresh_from_db()
        self.assertEqual(genre.name, "Thriller")

    def test_delete_genre(self):
        genre = Genre.objects.create(name="Action")
        response = self.client.delete(f"/api/cinema/genres/{genre.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Genre.objects.count(), 0)
