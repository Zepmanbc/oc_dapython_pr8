# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView, name='register'),
]
