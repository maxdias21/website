import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse, resolve
from django.test import TestCase
from blog import views

class BlogViewsTest(TestCase):
    # Teste Views
    def test_blog_create_post_view_is_correct(self):
        view = resolve('/blog/create_post/')

        self.assertEqual(view.func.view_class, views.CreatePost)

    def test_blog_all_posts_view_is_correct(self):
        view = resolve('/blog/all_posts/')

        self.assertEqual(view.func.view_class, views.ListPosts)

    def test_blog_read_post_view_is_correct(self):
        view = resolve(reverse('blog:read_post', kwargs={'slug': 'post1'}))

        self.assertEqual(view.func.view_class, views.ReadPost)

    def test_blog_all_users_view_is_correct(self):
        view = resolve('/blog/all_users/')

        self.assertEqual(view.func.view_class, views.ListUsers)

    def test_blog_search_view_is_correct(self):
        view = resolve('/blog/search/')

        self.assertEqual(view.func.view_class, views.Search)

    # Teste app_name e namespaces
    def test_blog_create_post_app_name_is_correct(self):
        view = resolve('/blog/create_post/')

        self.assertEqual(view.app_name, 'blog')

    # Teste app_name e namespaces
    def test_blog_create_post_namespace_is_correct(self):
        view = resolve('/blog/create_post/')

        self.assertEqual(view.url_name, 'create_post')

    # Testes URL_NAME
    def test_blog_create_post_url_name_is_correct(self):
        view = resolve('/blog/create_post/')

        self.assertEqual(view.url_name, 'create_post')

    def test_blog_all_posts_url_name__is_correct(self):
        view = resolve('/blog/all_posts/')

        self.assertEqual(view.url_name, 'all_posts')

    def test_blog_read_post_url_name_is_correct(self):
        view = resolve(reverse('blog:read_post', kwargs={'slug': 'post1'}))

        self.assertEqual(view.url_name, 'read_post')

    def test_blog_all_users_url_name_is_correct(self):
        view = resolve('/blog/all_users/')

        self.assertEqual(view.url_name, 'all_users')

    def test_blog_search_url_name__is_correct(self):
        view = resolve('/blog/search/')

        self.assertEqual(view.url_name, 'search')

