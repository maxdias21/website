import os
import django

# Configuração PyCharm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.urls import reverse, resolve
from django.test import TestCase
from authors import views

class AuthorsViewsTest(TestCase):
    # Testes Views
    def test_view_authors_login_is_correct(self):
        view = resolve('/authors/login/')

        self.assertEqual(view.func.view_class, views.Login)


    def test_view_authors_logout_is_correct(self):
        view = resolve('/authors/logout/')

        self.assertEqual(view.func.view_class, views.Logout)

    def test_view_authors_register_is_correct(self):
        view = resolve('/authors/register/')

        self.assertEqual(view.func.view_class, views.Register)

    def test_view_authors_my_profile_is_correct(self):
        view = resolve('/authors/myprofile/')

        self.assertEqual(view.func.view_class, views.MyProfile)

    def test_view_authors_create_profile_is_correct(self):
        view = resolve('/authors/create_profile/')

        self.assertEqual(view.func.view_class, views.CreateProfile)

    def test_view_authors_user_profile_is_correct(self):
        view = resolve(reverse('authors:user_profile', kwargs={'slug': 'user123'}))

        self.assertEqual(view.func.view_class, views.UserProfile)

    # Testes App_name e namespace
    def test_app_name_authors_is_correct(self):
        view = resolve('/authors/login/')

        self.assertEqual(view.app_name, 'authors')

    def test_namespace_authors_is_correct(self):
        view = resolve('/authors/login/')

        self.assertEqual(view.namespace, 'authors')

    # Testes url_name
    def test_url_name_authors_login_is_correct(self):
        view = resolve('/authors/login/')

        self.assertEqual(view.url_name, 'login')

    def test_url_name_authors_register_is_correct(self):
        view = resolve('/authors/register/')

        self.assertEqual(view.url_name, 'register')

    def test_url_name_authors_logout_is_correct(self):
        view = resolve('/authors/logout/')

        self.assertEqual(view.url_name, 'logout')

    def test_url_name_authors_create_profile_is_correct(self):
        view = resolve('/authors/create_profile/')

        self.assertEqual(view.url_name, 'create_profile')

    def test_url_name_authors_my_profile_is_correct(self):
        view = resolve('/authors/myprofile/')

        self.assertEqual(view.url_name, 'my_profile')

    def test_url_name_authors_user_profile_is_correct(self):
        view = resolve(reverse('authors:user_profile', kwargs={'slug': 'user123'}))

        self.assertEqual(view.url_name, 'user_profile')

