import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from utils.tests.base.create_author_or_user_mixin import CreateAuthorOrUser
from django.urls import reverse


class LogoutTest(CreateAuthorOrUser):
    def test_user_login_success(self):
        password = 'test123'
        username = self.create_user(password=password)

        response = self.client.post(reverse('authors:login'), data={
            'username': username.username,
            'password': password
        },
        follow = True)

        content = response.content.decode('utf-8')

        self.assertIn(f'Olá, {username.username}! Você fez login com sucesso!', content)

    def test_user_login_failed(self):
        password = 'test123'
        username = self.create_user(password=password)

        response = self.client.post(reverse('authors:login'), data={
            'username': username.username,
            'password': 'wrongPassword'
        },
                                    follow=True)

        content = response.content.decode('utf-8')

        self.assertIn(f'Seu usuário ou senha estão incorretos, tente novamente!', content)

