from .models import Post
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.username_a = 'user_a'
        self.username_b = 'user_b'

        self.password = 'testpassword'

        self.user_a = User.objects.create_user(
            username=self.username_a, password=self.password)

        response = self.client.post('/api/token/', {
            'username': self.username_a,
            'password': self.password
        })

        self.access_token = response.data['access']

    def test_create_post(self):
        data = {'title': 'Sample Post',
                'content': 'Sample Content',
                }

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post('/api/posts/', data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_unauthenticated_user_cannot_create_post(self):
        data = {'title': 'Sample Post',
                'content': 'Sample Content',
                }

        response = self.client.post('/api/posts/', data, format='json')

        self.assertEqual(response.status_code, 401)

    def test_create_update_delete_post(self):
        data = {'title': 'Sample Post',
                'content': 'Sample Content',
                }

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

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

        user_b = User.objects.create_user(
            username=self.username_b, password=self.password)

        post = Post.objects.create(
            title='Sample Post',
            content='Sample Content',
            author=user_b
        )

        id = post.id

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        update_response = self.client.put(f'/api/posts/{id}/')
        delete_response = self.client.delete(f'/api/posts/{id}/')

        self.assertEqual(update_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
