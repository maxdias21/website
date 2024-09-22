from django.urls import path
from . import views
from .views import MyProfile

app_name = 'authors'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('myprofile/', MyProfile.as_view(), name='my_profile'),
    path('create_profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('users/<slug:slug>/', views.UserProfile.as_view(), name='user_profile')
]
