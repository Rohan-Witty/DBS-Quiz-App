from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Option, Question, CorrectOption

def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    questions = Question.objects.all()
    options = Option.objects.all()
    correct_options = CorrectOption.objects.all()
    return render(request, 'quiz/quiz.html', {"Question": questions, "Option": options, "CorrectOption": correct_options})
