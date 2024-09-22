from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('all_posts/', views.ListPosts.as_view(), name='all_posts'),
    path('post/<slug:slug>/', views.ReadPost.as_view(), name='read_post'),
    path('all_users/', views.ListUsers.as_view(), name='all_users'),
    path('search/', views.Search.as_view(), name='search')
]
