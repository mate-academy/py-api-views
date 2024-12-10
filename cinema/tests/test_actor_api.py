from django.test import TestCase
from rest_framework import generics, mixins, status, viewsets
from rest_framework.test import APIClient

from cinema.models import Actor
from cinema.serializers import ActorSerializer
from cinema.views import ActorDetail, ActorList


class ActorApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Actor.objects.create(first_name="George", last_name="Clooney")
        Actor.objects.create(first_name="Keanu", last_name="Reeves")

    def test_actor_list_is_subclass(self):
        self.assertTrue(issubclass(ActorList, mixins.ListModelMixin))
        self.assertTrue(issubclass(ActorList, mixins.CreateModelMixin))
        self.assertTrue(issubclass(ActorList, generics.GenericAPIView))

    def test_actor_list_is_not_subclass(self):
        self.assertFalse(issubclass(ActorList, viewsets.GenericViewSet))

    def test_actor_detail_is_subclass(self):
        items = [
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            generics.GenericAPIView,
        ]

        for item in items:
            with self.subTest():
                self.assertTrue(issubclass(ActorDetail, item))

    def test_actor_detail_is_not_subclass(self):
        self.assertFalse(issubclass(ActorDetail, viewsets.GenericViewSet))

    def test_get_actors(self):
        response = self.client.get("/api/cinema/actors/")
        serializer = ActorSerializer(Actor.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_actors(self):
        response = self.client.post(
            "/api/cinema/actors/",
            {
                "first_name": "Scarlett",
                "last_name": "Johansson",
            },
        )
        db_actors = Actor.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(db_actors.count(), 3)
        self.assertEqual(db_actors.filter(first_name="Scarlett").count(), 1)

    def test_get_actor(self):
        response = self.client.get("/api/cinema/actors/2/")
        serializer = ActorSerializer(
            Actor(id=2, first_name="Keanu", last_name="Reeves")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_actor(self):
        response = self.client.get("/api/cinema/actors/1001/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_actor(self):
        response = self.client.put(
            "/api/cinema/actors/1/",
            {
                "first_name": "Scarlett",
                "last_name": "Johansson",
            },
        )
        actor_pk_1 = Actor.objects.get(pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [
                actor_pk_1.first_name,
                actor_pk_1.last_name,
            ],
            [
                "Scarlett",
                "Johansson",
            ],
        )

    def test_patch_actor(self):
        response = self.client.patch(
            "/api/cinema/actors/1/",
            {
                "first_name": "Scarlett",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_actor(self):
        response = self.client.delete(
            "/api/cinema/actors/1/",
        )
        db_actors_id_1 = Actor.objects.filter(id=1)
        self.assertEqual(db_actors_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_actor(self):
        response = self.client.delete(
            "/api/cinema/actors/1000/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
