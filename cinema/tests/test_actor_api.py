from django.test import TestCase
from django.urls import reverse

from rest_framework import status, generics, mixins, viewsets
from rest_framework.test import APIClient, APITestCase

from cinema.serializers import ActorSerializer
from cinema.models import Actor
from cinema.views import (ActorListCreate as ActorList,
                          ActorRetrieveUpdateDestroy as ActorDetail)


class ActorApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Actor.objects.all().delete()
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
        url = reverse('cinema:actor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_actors(self):
        url = reverse('cinema:actor-list')
        data = {"first_name": "John", "last_name": "Doe"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 3)  # Początkowo 2, dodajemy 1
        self.assertEqual(Actor.objects.last().first_name, "John")

    def test_get_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        url = reverse("cinema:actor-detail", args=[actor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_actor(self):
        response = self.client.get(reverse('cinema:actor-detail', args=[1001]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        url = reverse('cinema:actor-detail', args=[actor.id])
        data = {"first_name": "Jane", "last_name": "Doe"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actor.refresh_from_db()
        self.assertEqual(actor.first_name, "Jane")

    def test_patch_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        url = reverse('cinema:actor-detail', args=[actor.id])
        data = {"first_name": "Jane"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actor.refresh_from_db()
        self.assertEqual(actor.first_name, "Jane")

    def test_delete_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        url = reverse('cinema:actor-detail', args=[actor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Actor.objects.count(), 2)

    def test_delete_invalid_actor(self):
        response = self.client.delete(reverse('cinema:actor-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
