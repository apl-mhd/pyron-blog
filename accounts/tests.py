from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class PostAPITestCase(APITestCase):

    def setUp(self):
        self.username = 'user'
        self.password = 'testpassword'

        self.user = User.objects.create_user(
            username=self.username, password=self.password)

        response = self.client.post('/api/token/', {
            'username': self.username,
            'password': self.password
        })

        access_token = access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_create_user(self):
        data = {
            'username': 'username',
            'email': 'email@mail.com',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password': 'password',
            'confirm_password': 'password',
        }
        response = self.client.post('/api/register/', data=data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_create_user_wrong_password(self):
        data = {
            'username': 'username',
            'email': 'email@mail.com',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password': 'password',
            'confirm_password': 'wrong_password',
        }

        response = self.client.post('/api/register/', data=data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_login(self):
        response = self.client.post('/api/token/', {
            'username': self.username,
            'password': self.password
        })

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_fail(self):
        response = self.client.post('/api/token/', {
            'username': self.username,
            'password': 'wrong password',
        })

        self.assertEqual(response.status_code, 401)
