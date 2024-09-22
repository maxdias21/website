import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse
from django.test import TestCase


class NewsUrlsTest(TestCase):
    def test_url_login_is_correct(self):
        login_url = reverse('authors:login')

        self.assertEqual('/authors/login/', login_url)

    def test_url_register_is_correct(self):
        login_url = reverse('authors:register')

        self.assertEqual('/authors/register/', login_url)

    def test_url_logout_is_correct(self):
        login_url = reverse('authors:logout')

        self.assertEqual('/authors/logout/', login_url)

    def test_url_my_profile_is_correct(self):
        login_url = reverse('authors:my_profile')

        self.assertEqual('/authors/myprofile/', login_url)

    def test_url_create_profile_is_correct(self):
        login_url = reverse('authors:my_profile')

        self.assertEqual('/authors/myprofile/', login_url)

    def test_url_users_profile_is_correct(self):
        login_url = reverse('authors:user_profile', kwargs={'slug':'user123'})

        self.assertEqual('/authors/users/user123/', login_url)

