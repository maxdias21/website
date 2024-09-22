from django.contrib.auth.models import User
from authors.models import Authors
from django.test import TestCase


class CreateAuthorOrUser(TestCase):
    @staticmethod
    def create_user(first_name='first', last_name='last', username='user123', email='test@test.com',
                    password='password'):
        return User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password)

    def create_author(self, username=None, age=0, hometown='Acre', current_city='Acre', sex='M',
                      marital_status='S',
                      description='description', profile_status='Público', is_active=True):
        if not username:
            username = self.create_user()

        return Authors.objects.create(username=username, hometown=hometown, age=age, current_city=current_city, sex=sex,
                                      marital_status=marital_status, description=description,
                                      profile_status=profile_status, is_active=is_active)
