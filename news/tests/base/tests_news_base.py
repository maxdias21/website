from news.models import News
from django.test import TestCase
from django.contrib.auth.models import User
from ...models import NewsType

from typing import List


class RecipeMixin():
    def create_user(self, first_name='first', last_name='last', username='user123', email='test@test.com',
                    password='password'):
        return User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password)

    def make_news(self, author=None, title='Title', description='Description', content='Content',
                  image='No image', is_published=True, slug='slug', type_news_name='N'):

        accepted_types = ['N', 'M', 'S', 'T']

        news = News.objects.create(author=author, title=title, description=description, content=content, image=image,
                                   is_published=is_published, slug=slug)

        if type_news_name:
            type_news = accepted_types if type_news_name.upper() in accepted_types else 'N'

            main_news_type, created = NewsType.objects.get_or_create(type_news=type_news)
            news.type_news.add(main_news_type)

        if not author:
            user = self.create_user()

        return news


class NewsTestBase(TestCase, RecipeMixin):
    ...
