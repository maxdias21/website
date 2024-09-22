from django.utils.translation import gettext_lazy
from utils.models.BasePost import BasePost
from django.db import models


class NewsType(models.Model):
    type_news = models.CharField(choices=(('M', 'MainNews'), ('S', 'SecondaryNews'), ('T', 'ThirdNews'), ('N','Normal')), max_length=20, default='N')

    def __str__(self):
        return self.get_type_news_display()



class News(BasePost):
    type_news = models.ManyToManyField(NewsType)

    class Meta:
        verbose_name_plural = gettext_lazy('News')
        verbose_name = gettext_lazy('News')
