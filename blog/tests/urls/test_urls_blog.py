import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.test import TestCase
from django.urls import reverse

class BlogUrlsTest(TestCase):
    def test_url_create_post_is_correct(self):
        url = reverse('blog:create_post')

        self.assertEqual(url,'/blog/create_post/')


    def test_url_all_posts_is_correct(self):
        url = reverse('blog:all_posts')

        self.assertEqual(url, '/blog/all_posts/')

    def test_url_read_post_is_correct(self):
        slug = 'post1'
        url = reverse('blog:read_post', kwargs={'slug': slug})

        self.assertEqual(url, f'/blog/post/{slug}/')

    def test_url_all_users_is_correct(self):
        url = reverse('blog:all_users')

        self.assertEqual(url, '/blog/all_users/')

    def test_url_search_is_correct(self):
        url = reverse('blog:search')

        self.assertEqual(url, '/blog/search/')