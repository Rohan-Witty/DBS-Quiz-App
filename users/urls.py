from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name ='users-login'),
    path('register/', views.register_page, name ='users-register'),
]