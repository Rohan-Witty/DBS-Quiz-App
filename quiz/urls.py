from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='quiz-home'),
    path('quiz/', views.quiz, name ='quiz-quiz'),
]
