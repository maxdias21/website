from blog.models import PostBlog
from utils.tests.base.create_author_or_user_mixin import CreateAuthorOrUser
from django.test import TestCase

class CreatePostBlog(TestCase):
    @staticmethod
    def make_post_blog(author=None, title='Title', description='Description', content='Content',
                  image='No image', is_published=True, slug='slug'):

        if not author:
            author = CreateAuthorOrUser.create_user()

        return PostBlog.objects.create(author=author, title=title, description=description, content=content, image=image,
                                   is_published=is_published, slug=slug)

