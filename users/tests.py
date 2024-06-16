from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import User

class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('registration')

    def test_registration_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'testuser')

    def test_registration_existing_user(self):
        existing_user = User.objects.create(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'newpassword'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['code'], 400)
        self.assertEqual(response.data['answer'], 'A user with the same name already exists')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().password, 'testpassword')

    def test_registration_invalid_data(self):
        data = {
            'username': '',
            'password': ''
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


class FavoritesViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.favorites_url = reverse('getFavorites')


    def test_get_favorites_user_not_found(self):
        User.objects.create(username='testuser', password='testpassword', favorites='1,2,3')
        url = f'{self.favorites_url}?username=unknownuser'
        response = self.client.get(url)
        self.assertEqual(response.data['code'], 500)
        self.assertEqual(response.data['answer'], 'something went wrong, try to relogin')

