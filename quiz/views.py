from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Option, Question

def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    results = Question.objects.all()
    res = Option.objects.all()
    return render(request, 'quiz/quiz.html', {"Question": results, "Option": res})
