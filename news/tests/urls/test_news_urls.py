import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse, resolve
from ..base.tests_news_base import NewsTestBase


class NewsUrlsTest(NewsTestBase):
    def test_url_index_is_correct(self):
        news_url = reverse('news:index')

        self.assertEqual('/', news_url)

    def test_url_all_news_is_correct(self):
        all_news_url = reverse('news:all_news')

        self.assertEqual('/news/all_news/', all_news_url)

    def test_url_read_news_url_is_correct(self):

        read_news_url = reverse('news:read_news', kwargs={'slug': 'news1'})

        self.assertEqual(f'/news/news1/', read_news_url)
