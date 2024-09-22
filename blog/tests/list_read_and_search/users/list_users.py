import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse
from utils.tests.base.create_author_or_user_mixin import CreateAuthorOrUser

class UserListTest(CreateAuthorOrUser):
    def setUp(self):
        self.author = self.create_author()

    def test_show_a_profile_if_is_active_is_true(self):
        response = self.client.get(reverse('blog:all_users'))

        content = response.content.decode('utf-8')

        self.assertIn('user123', content)

    def test_not_show_a_profile_if_is_active_is_false(self):
        username = self.create_user(username='teste1', email='tes1@gmail.com')
        self.create_author(username=username, is_active=False)

        response = self.client.get(reverse('blog:all_posts'))

        content = response.content.decode('utf-8')

        self.assertNotIn('Title', content)

