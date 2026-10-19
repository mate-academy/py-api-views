from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from cinema.models import Actor, Genre, Movie


class ApiValidationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor = Actor.objects.create(first_name="Keanu", last_name="Reeves")
        self.genre = Genre.objects.create(name="Action")
        self.movie = Movie.objects.create(
            title="The Matrix", description="A simulation", duration=136
        )

    def test_movie_relationships_create_replace_and_clear(self):
        response = self.client.post(
            "/api/cinema/movies/",
            {
                "title": "Speed",
                "description": "A bus",
                "duration": 116,
                "actors": [self.actor.pk],
                "genres": [self.genre.pk],
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        movie_url = f"/api/cinema/movies/{response.data['id']}/"
        self.assertEqual(response.data["actors"], [self.actor.pk])
        self.assertEqual(response.data["genres"], [self.genre.pk])

        replacement = Actor.objects.create(first_name="Sandra", last_name="Bullock")
        response = self.client.put(
            movie_url,
            {
                "title": "Speed",
                "description": "A bus",
                "duration": 116,
                "actors": [replacement.pk],
                "genres": [self.genre.pk],
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["actors"], [replacement.pk])

        response = self.client.patch(
            movie_url, {"actors": [], "genres": []}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie = Movie.objects.get(pk=response.data["id"])
        self.assertFalse(movie.actors.exists())
        self.assertFalse(movie.genres.exists())
        self.assertEqual(movie.duration, 116)

    def test_invalid_movie_relationship_does_not_update_movie(self):
        for field in ("actors", "genres"):
            with self.subTest(field=field):
                response = self.client.patch(
                    f"/api/cinema/movies/{self.movie.pk}/",
                    {"title": "Changed", field: [99999]},
                    format="json",
                )
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertIn(field, response.data)
                self.movie.refresh_from_db()
                self.assertEqual(self.movie.title, "The Matrix")

    def test_duplicate_genre_is_rejected_on_create_and_update(self):
        other = Genre.objects.create(name="Drama")
        response = self.client.post(
            "/api/cinema/genres/", {"name": self.genre.name}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.patch(
            f"/api/cinema/genres/{other.pk}/", {"name": self.genre.name}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        other.refresh_from_db()
        self.assertEqual(other.name, "Drama")

    def test_missing_required_fields_are_rejected_for_each_entity(self):
        for entity in ("genres", "actors", "cinema_halls", "movies"):
            with self.subTest(entity=entity):
                response = self.client.post(
                    f"/api/cinema/{entity}/", {}, format="json"
                )
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertTrue(response.data)

    def test_missing_updates_return_not_found_for_each_entity(self):
        for entity in ("genres", "actors", "cinema_halls", "movies"):
            for method in ("put", "patch"):
                with self.subTest(entity=entity, method=method):
                    response = getattr(self.client, method)(
                        f"/api/cinema/{entity}/99999/", {}, format="json"
                    )
                    self.assertEqual(
                        response.status_code, status.HTTP_404_NOT_FOUND
                    )
