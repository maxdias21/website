import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()


from tests.functional_tests.authors.base import SeleniumBaseTest
from django.urls import reverse
from utils.tests.base.create_author_or_user_mixin import CreateAuthorOrUser
from selenium.webdriver.common.by import By

class AuthorsLoginTest(SeleniumBaseTest):
    def test_user_can_logout_successfully(self):
        username = 'Tes123'
        password = 'Password123'

        self.browser.get(self.live_server_url + reverse('authors:login'))

        CreateAuthorOrUser.create_user(username=username, password=password)

        form = self.browser.find_element(By.ID, 'form')

        username_field= form.find_element(By.XPATH, '//*[@id="username"]')
        username_field.send_keys(username)

        password_field = form.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys(password)

        form.submit()

        form_logout = self.browser.find_element(By.ID, 'logout')

        form_logout.submit()

        body = self.browser.find_element(By.TAG_NAME, 'body').text

        self.assertIn('Você saiu da sua conta com sucesso!', body)

    def test_user_cannot_logout_using_get_method(self):
        username = 'Tes123'
        password = 'Password123'

        self.browser.get(self.live_server_url + reverse('authors:logout'))

        body = self.browser.find_element(By.TAG_NAME, 'body').text

        self.assertIn('Houve um erro ao sair da sua conta!', body)



