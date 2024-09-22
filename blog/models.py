from django.utils.translation import gettext_lazy
from utils.models.BasePost import BasePost

# Create your models here.

class PostBlog(BasePost):
    class Meta:
        verbose_name_plural = gettext_lazy('Post Blog')
        verbose_name = gettext_lazy('Post Blog')

