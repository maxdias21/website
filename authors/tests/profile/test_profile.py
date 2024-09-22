import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from utils.tests.base.create_author_or_user_mixin import CreateAuthorOrUser
from django.urls import reverse
from utils.tests.base.create_post_blog import CreatePostBlog


class TestProfile(CreateAuthorOrUser):
    def setUp(self):
        self.password = 'password123'

    def test_cannot_acess_profile_if_not_exists(self):
        user = self.create_user(password=self.password)

        self.client.login(username=user.username, password=self.password)

        response = self.client.get(reverse('authors:my_profile'), follow=True)

        content = response.content.decode('utf-8')

        self.assertIn('Parece que você ainda não possui um perfil. Vamos criar um agora!', content)

    def test_show_profile_informations(self):
        fields = {
            'age': 0,
            'hometown': 'Acre',
            'current_city': 'Acre',
            'sex': 'M',
            'marital_status': 'S',
            'description': 'description',
            'profile_status': 'Público'
        }

        user = self.create_user(password=self.password)
        author = self.create_author(username=user)

        self.client.login(username=user.username, password=self.password)

        response = self.client.get(reverse('authors:my_profile'), follow=True)

        content = response.content.decode('utf-8')


        for items in fields:
            with self.subTest(msg=items):
                self.assertIn(items, content)


    def test_show_msg_no_posts_if_author_does_not_have_a_post(self):
        user = self.create_user(password=self.password)
        author = self.create_author(username=user)

        self.client.login(username=user.username, password=self.password)

        response = self.client.get(reverse('authors:my_profile'), follow=True)

        content = response.content.decode('utf-8')

        self.assertIn('Você ainda não publicou nada :(', content)

    def test_show_post_if_author_have_a_post(self):
        user = self.create_user(password=self.password)
        author = self.create_author(username=user)

        post = CreatePostBlog.make_post_blog(author=author.username)

        self.client.login(username=user.username, password=self.password)

        response = self.client.get(reverse('authors:my_profile'), follow=True)

        content = response.content.decode('utf-8')

        self.assertIn(post.title, content)


