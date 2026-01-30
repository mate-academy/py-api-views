from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from cinema.models import Movie, Genre, Actor
from cinema.serializers import MovieSerializer

MOVIE_URL = "/api/cinema/movies/"

def detail_url(movie_id):
    return f"{MOVIE_URL}{movie_id}/"

class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="Jack", last_name="Nicholson")

        self.movie = Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=200,
        )
        self.movie.genres.add(self.genre)
        self.movie.actors.add(self.actor)

    # --- GET Тести ---
    def test_list_movies(self):
        res = self.client.get(MOVIE_URL)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_movie_detail(self):
        url = detail_url(self.movie.id)
        res = self.client.get(url)
        serializer = MovieSerializer(self.movie)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    # --- POST Тест ---
    def test_post_movies(self):
        payload = {
            "title": "Superman",
            "description": "Superman description",
            "duration": 170,
            "genres": [self.genre.id],
            "actors": [self.actor.id],
        }
        response = self.client.post(MOVIE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2) # 1 з setUp + 1 новий

    # --- PUT/PATCH Тести ---
    def test_put_movie(self):
        payload = {
            "title": "Watchman",
            "description": "Watchman description",
            "duration": 190,
            "genres": [self.genre.id],
            "actors": [self.actor.id],
        }
        url = detail_url(self.movie.id)
        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Watchman")

    def test_patch_movie(self):
        url = detail_url(self.movie.id)
        response = self.client.patch(url, {"title": "New Title"})
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "New Title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- DELETE Тест ---
    def test_delete_movie(self):
        url = detail_url(self.movie.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())
