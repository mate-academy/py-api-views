from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from cinema.serializers import MovieSerializer
from cinema.models import Movie, Actor, Genre
from cinema.views import MovieViewSet
from rest_framework.viewsets import ModelViewSet


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.actor1 = Actor.objects.create(first_name="John", last_name="Doe")
        self.actor2 = Actor.objects.create(first_name="Jane", last_name="Doe")
        self.genre1 = Genre.objects.create(name="Action")
        self.genre2 = Genre.objects.create(name="Comedy")

        Movie.objects.all().delete()

        self.movie1 = Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=200,
            rating=4.5,
        )
        self.movie1.actors.add(self.actor1, self.actor2)
        self.movie1.genres.add(self.genre1, self.genre2)

        self.movie2 = Movie.objects.create(
            title="Batman",
            description="Batman description",
            duration=190,
            rating=4.0,
        )
        self.movie2.actors.add(self.actor1, self.actor2)
        self.movie2.genres.add(self.genre1, self.genre2)

    def test_movie_viewset_is_subclass_model_viewset(self):
        self.assertTrue(issubclass(MovieViewSet, ModelViewSet))

    def test_get_movies(self):
        url = reverse('cinema:movie-list')
        response = self.client.get(url)
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_movies(self):
        url = reverse('cinema:movie-list')
        data = {
            "title": "Superman",
            "description": "Superman description",
            "duration": 170,
            "rating": 4.7,
            "actors": [self.actor1.id, self.actor2.id],
            "genres": [self.genre1.id, self.genre2.id],
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)
        self.assertEqual(Movie.objects.filter(title="Superman").count(), 1)

    def test_post_invalid_movies(self):
        url = reverse('cinema:movie-list')
        data = {
            "title": "Superman",
            "description": "Superman description",
            "duration": "two hundred",
        }
        response = self.client.post(url, data, format='json')
        superman_movies = Movie.objects.filter(title="Superman")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(superman_movies.count(), 0)

    def test_get_movie(self):
        url = reverse('cinema:movie-detail', args=[self.movie2.id])
        response = self.client.get(url)
        serializer = MovieSerializer(self.movie2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_movie(self):
        url = reverse('cinema:movie-detail', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movie(self):
        url = reverse('cinema:movie-detail', args=[self.movie1.id])
        data = {
            "title": "Watchman",
            "description": "Watchman description",
            "duration": 190,
            "rating": 4.8,
            "actors": [self.actor1.id, self.actor2.id],
            "genres": [self.genre1.id, self.genre2.id],
        }
        response = self.client.put(url, data, format='json')
        print(response.data)
        db_movie = Movie.objects.get(id=self.movie1.id)
        self.assertEqual(db_movie.title, "Watchman")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_movie(self):
        url = reverse('cinema:movie-detail', args=[self.movie1.id])
        data = {
            "title": "Watchmen",
            "description": "Watchmen description",
            "duration": "fifty",
        }
        response = self.client.put(url, data, format='json')
        db_movie = Movie.objects.get(id=self.movie1.id)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_movie(self):
        url = reverse('cinema:movie-detail', args=[self.movie1.id])
        data = {
            "title": "Watchmen",
        }
        response = self.client.patch(url, data, format='json')
        db_movie = Movie.objects.get(id=self.movie1.id)
        self.assertEqual(db_movie.title, "Watchmen")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_movie(self):
        url = reverse('cinema:movie-detail', args=[self.movie1.id])
        data = {
            "duration": "invalid_value",
        }
        response = self.client.patch(url, data, format='json')
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         f"Expected 400 BAD REQUEST but got {response.status_code} instead. "
                         f"Response data: {response.data}")

    def test_delete_movie(self):
        url = reverse('cinema:movie-detail', args=[self.movie1.id])
        response = self.client.delete(url)
        db_movies_id_1 = Movie.objects.filter(id=self.movie1.id)
        self.assertEqual(db_movies_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_movie(self):
        url = reverse('cinema:movie-detail', args=[1000])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
