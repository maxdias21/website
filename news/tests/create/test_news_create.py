import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse

from ..base.tests_news_base import NewsTestBase

from utils.tests.base.create_author_or_user_mixin import  CreateAuthorOrUser


class NewsCreateTest(NewsTestBase, CreateAuthorOrUser):
    def test_news_template_loads_news(self):
        news = self.make_news()

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertIn(news.title, content)

    def test_news_template_loads_main_news(self):
        news = self.make_news(type_news_name='M')

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertIn(news.title, content)

    def test_news_template_loads_secondary_news(self):
        news = self.make_news(type_news_name='S')

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertIn(news.title, content)

    def test_news_template_loads_third_news(self):
        news = self.make_news(type_news_name='T')

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertIn(news.title, content)

    def test_news_template_not_show_if_is_not_published_is_false(self):
        news = self.make_news(is_published=False)

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertNotIn(news.title, content)

    def test_new_user_shows_in_template(self):
        author = self.create_author()

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertIn(author.username.first_name, content)

    def test_new_user_not_shows_in_template_if_is_active_is_false(self):
        author = self.create_author(is_active=False)

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertNotIn(author.username.first_name, content)


    def test_new_user_not_show_if_not_have_a_profile(self):
        user = self.create_user()

        response = self.client.get(reverse('news:index'))

        content = response.content.decode('utf-8')

        self.assertNotIn(user.first_name, content)


