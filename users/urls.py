from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user-settings', views.user_settings, name='user_settings')
]
