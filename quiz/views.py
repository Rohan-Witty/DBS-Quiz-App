from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Exam

def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    results = Exam.objects.all()
    return render(request, 'quiz/quiz.html', {"Exam": results})
