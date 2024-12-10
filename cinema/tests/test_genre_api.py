from django.test import TestCase
from rest_framework import generics, status, viewsets
from rest_framework.test import APIClient
from rest_framework.views import APIView

from cinema.models import Genre
from cinema.serializers import GenreSerializer
from cinema.views import GenreDetail, GenreList


class GenreApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Genre.objects.create(
            name="Comedy",
        )
        Genre.objects.create(
            name="Drama",
        )

    def test_genre_list_is_subclass(self):
        self.assertTrue(issubclass(GenreList, APIView))

    def test_genre_list_is_not_subclass(self):
        items = [generics.GenericAPIView, viewsets.GenericViewSet]

        for item in items:
            with self.subTest(str(item).split(".")[2]):
                self.assertFalse(issubclass(GenreList, item))

    def test_genre_detail_is_subclass(self):
        self.assertTrue(issubclass(GenreDetail, APIView))

    def test_genre_detail_is_not_subclass(self):
        items = [generics.GenericAPIView, viewsets.GenericViewSet]

        for item in items:
            with self.subTest(str(item).split(".")[2]):
                self.assertFalse(issubclass(GenreDetail, item))

    def test_get_genres(self):
        response = self.client.get("/api/cinema/genres/")
        serializer = GenreSerializer(Genre.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_genres(self):
        response = self.client.post(
            "/api/cinema/genres/",
            {
                "name": "Sci-fi",
            },
        )
        db_genres = Genre.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(db_genres.count(), 3)
        self.assertEqual(db_genres.filter(name="Sci-fi").count(), 1)

    def test_get_genre(self):
        response = self.client.get("/api/cinema/genres/2/")
        serializer = GenreSerializer(
            Genre(
                id=2,
                name="Drama",
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_genre(self):
        response = self.client.get("/api/cinema/genres/1001/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_genre(self):
        response = self.client.put(
            "/api/cinema/genres/1/",
            {
                "name": "Sci-fi",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_genre(self):
        response = self.client.patch(
            "/api/cinema/genres/1/",
            {
                "name": "Sci-fi",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_genre(self):
        response = self.client.delete(
            "/api/cinema/genres/1/",
        )
        db_genres_id_1 = Genre.objects.filter(id=1)
        self.assertEqual(db_genres_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_genre(self):
        response = self.client.delete(
            "/api/cinema/genres/1000/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
