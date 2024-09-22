import django
import os
from unittest import TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from authors.tests.test_authors_base import AuthorMixin
from django.urls import reverse
from ..forms.register import RegisterForm

class AuthorRegisterForm(AuthorMixin):
    def setUp(self):
        self.fields = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha',
            'username': 'Usuário',
        }
        
    def test_fields_placeholder_is_correct(self):
        form = RegisterForm()

        for key in self.fields.items():
            with self.subTest(key):
                placeholder = form[key[0]].field.widget.attrs['placeholder']
                self.assertEqual(key[1], placeholder)


