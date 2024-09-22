import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse, resolve
from django.test import TestCase
from news import views


class NewsViewsTest(TestCase):
    # Testes Views
    def test_news_view_index_is_correct(self):
        view = resolve('/')

        self.assertIs(view.func.view_class, views.News)

    def test_all_news_view_is_correct(self):
        view = resolve('/news/all_news/')

        self.assertEqual(view.func.view_class, views.AllNews)

    def test_read_news_view_is_correct(self):
        view = resolve(reverse('news:read_news', kwargs={'slug': 'news1'}))

        self.assertEqual(view.func.view_class, views.ReadNews)

    # Testes App_name e namespace
    def test_news_index_app_name_is_correct(self):
        view = resolve('/')

        self.assertIs(view.app_name, 'news')

    def test_news_index_namespace_is_correct(self):
        view = resolve('/')

        self.assertIs(view.namespace, 'news')

    # Testes URL_NAME
    def test_news_index_url_name_is_correct(self):
        view = resolve('/')

        self.assertIs(view.namespace, 'news')

    def test_news_all_news_url_name_is_correct(self):
        view = resolve('/news/all_news/')

        self.assertIs(view.url_name, 'all_news')

    def test_news_read_news_url_name_is_correct(self):
        view = resolve(reverse('news:read_news', kwargs={'slug': 'news1'}))

        self.assertIs(view.url_name, 'read_news')
