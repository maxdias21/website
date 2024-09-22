from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.News.as_view(), name='index'),
    path('news/all_news/', views.AllNews.as_view(), name='all_news'),
    path('news/<slug:slug>/', views.ReadNews.as_view(), name='read_news'),
]
