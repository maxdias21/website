import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from utils.tests.base.create_author_or_user_mixin import CreateAuthorOrUser
from django.urls import reverse


class TestLogout(CreateAuthorOrUser):
    def test_user_tries_to_logout_using_get_method(self):
        password = 'test123'
        username = self.create_user(password=password)

        self.client.login(username=username, password=password)

        response = self.client.get(reverse('authors:logout'), follow=True)

        content = response.content.decode('utf-8')

        self.assertIn('Houve um erro ao sair da sua conta!', content)

    def test_user_tries_logout_using_another_username(self):
        password = 'test123'
        username = self.create_user(password=password)

        self.client.login(username=username, password=password)

        response = self.client.post(reverse('authors:logout'), follow=True, data={
            'username': 'AnotherUsername'
        })

        content = response.content.decode('utf-8')

        self.assertIn('Ocorreu um erro ao tentar sair da conta. Por favor, tente novamente.', content)

    def test_user_tries_logout_successfully(self):
        password = 'test123'
        username = self.create_user(password=password)

        self.client.login(username=username, password=password)

        response = self.client.post(reverse('authors:logout'), follow=True, data={
            'username': username.username,
        })

        content= response.content.decode('utf-8')

        self.assertIn('Você saiu da sua conta com sucesso!', content)
