from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import time
from django.core.validators import ValidationError

# Create your models here.

class BasePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='news/covers/%Y/%m/%d',null=True, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=False, max_length=255)

    def clean(self):
        if not (self.slug):
            try:
                self.slug = slugify(f'{self.title}/f{time.time()}')
            except:
                raise ValidationError

    # Permite herança o abstract
    class Meta:
        abstract = True

    def __str__(self):
        return self.title