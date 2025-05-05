from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.username_a = 'user_a'
        self.username_b = 'user_b'

        self.password = 'testpassword'

        self.user_a = User.objects.create_user(
            username=self.username_a, password=self.password)

        self.user_b = User.objects.create_user(
            username=self.username_b, password=self.password)

        response = self.client.post('/api/token/', {
            'username': self.username_a,
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

    def test_login(self):
        response = self.client.post('/api/token/', {
            'username': self.username_a,
            'password': self.password
        })

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_fail(self):
        response = self.client.post('/api/token/', {
            'username': self.username_a,
            'password': 'wrong password',
        })

        self.assertEqual(response.status_code, 401)

    def test_create_post(self):
        data = {'title': 'Sample Post',
                'content': 'Sample Content',
                }

        response = self.client.post('/api/posts/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_update_delete_post(self):
        data = {'title': 'Sample Post',
                'content': 'Sample Content',
                }
        create_response = self.client.post(
            '/api/posts/', data=data, format='json')

        id = create_response.data['id']

        update_response = self.client.patch(
            f'/api/posts/{id}/', data=data, format='json')

        delete_response = self.client.delete(
            f'/api/posts/{id}/', data=data, format='json')

        self.assertEqual(create_response.status_code, 201)
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(delete_response.status_code, 204)

    def test_retrive_post(self):
        post = Post.objects.create(
            title='Sample Post',
            content='Sample Content',
            author=self.user_a
        )

        response = self.client.get(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_update_delete_another_users_post(self):

        post = Post.objects.create(
            title='Sample Post',
            content='Sample Content',
            author=self.user_b
        )

        id = post.id

        update_response = self.client.put(f'/api/posts/{id}/')
        delete_response = self.client.delete(f'/api/posts/{id}/')

        self.assertEqual(update_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
