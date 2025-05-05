from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class PostAPITestCase(APITestCase):
    def seTup(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
        self.url = reverse('api_posts_retrieve_update_destroy', args=[self.post.id])
        # self.user = User.objects.create_user(
        #     username='testuser', password='testpassword'
        # )
        # self.client.login(username='testuser', password='testpassword')
        # self.post = Post.objects.create(
        #     title='Test Post',
        #     content='This is a test post.',
        #     author=self.user
        # )


    def test_create_post(self):
        response = self.client.get(self.url)