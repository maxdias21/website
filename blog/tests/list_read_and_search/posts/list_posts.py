import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse
from utils.tests.base.create_post_blog import CreatePostBlog

class PostListTest(CreatePostBlog):
    def test_show_a_post_if_is_published_is_true(self):
        CreatePostBlog.make_post_blog()

        response = self.client.get(reverse('blog:all_posts'))

        content = response.content.decode('utf-8')

        self.assertIn('Title', content)

    def test_post_not_show_if_is_published_is_false(self):
        CreatePostBlog.make_post_blog(is_published=False)

        response = self.client.get(reverse('blog:all_posts'))

        content = response.content.decode('utf-8')

        self.assertNotIn('Title', content)

