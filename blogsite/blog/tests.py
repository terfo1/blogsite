from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment
from django.urls import reverse
from django.contrib.auth.models import User

class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='Test Content', published_date='2024-01-01T00:00:00Z')

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'New Content', 'published_date': '2024-01-01T00:00:00Z'}
        response = self.client.post(reverse('post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='Test Content', published_date='2024-01-01T00:00:00Z')
        self.comment = Comment.objects.create(post=self.post, author_name='Author', comment_text='Test Comment')

    def test_create_comment(self):
        data = {'post': self.post.id, 'author_name': 'Author', 'comment_text': 'New Comment'}
        response = self.client.post(reverse('comment-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comments(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
