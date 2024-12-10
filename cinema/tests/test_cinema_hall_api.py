from django.test import TestCase
from rest_framework import status, viewsets
from rest_framework.test import APIClient

from cinema.models import CinemaHall
from cinema.serializers import CinemaHallSerializer
from cinema.views import CinemaHallViewSet


class CinemaHallApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        CinemaHall.objects.create(
            name="Blue",
            rows=15,
            seats_in_row=20,
        )
        CinemaHall.objects.create(
            name="VIP",
            rows=6,
            seats_in_row=8,
        )

    def test_cinema_hall_is_subclass_generic_viewset(self):
        self.assertTrue(issubclass(CinemaHallViewSet, viewsets.GenericViewSet))

    def test_cinema_hall_is_not_subclass(self):
        self.assertFalse(issubclass(CinemaHallViewSet, viewsets.ModelViewSet))

    def test_get_cinema_halls(self):
        response = self.client.get("/api/cinema/cinema_halls/")
        serializer = CinemaHallSerializer(CinemaHall.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_cinema_halls(self):
        response = self.client.post(
            "/api/cinema/cinema_halls/",
            {
                "name": "Yellow",
                "rows": 14,
                "seats_in_row": 15,
            },
        )
        db_cinema_halls = CinemaHall.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(db_cinema_halls.count(), 3)
        self.assertEqual(db_cinema_halls.filter(name="Yellow").count(), 1)

    def test_get_cinema_hall(self):
        response = self.client.get("/api/cinema/cinema_halls/2/")
        serializer = CinemaHallSerializer(
            CinemaHall(
                id=2,
                name="VIP",
                rows=6,
                seats_in_row=8,
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_cinema_hall(self):
        response = self.client.get("/api/cinema/cinema_halls/1001/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_cinema_hall(self):
        response = self.client.put(
            "/api/cinema/cinema_halls/1/",
            {
                "name": "Yellow",
                "rows": 14,
                "seats_in_row": 15,
            },
        )
        cinema_hall_pk_1 = CinemaHall.objects.get(pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [
                cinema_hall_pk_1.name,
                cinema_hall_pk_1.rows,
                cinema_hall_pk_1.seats_in_row,
            ],
            [
                "Yellow",
                14,
                15,
            ],
        )

    def test_patch_cinema_hall(self):
        response = self.client.patch(
            "/api/cinema/cinema_halls/1/",
            {
                "name": "Green",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CinemaHall.objects.get(id=1).name, "Green")

    def test_delete_cinema_hall(self):
        response = self.client.delete(
            "/api/cinema/cinema_halls/1/",
        )
        db_cinema_halls_id_1 = CinemaHall.objects.filter(id=1)
        self.assertEqual(db_cinema_halls_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_cinema_hall(self):
        response = self.client.delete(
            "/api/cinema/cinema_halls/1000/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
