from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Option, Question, CorrectOption
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'quiz/home.html', {'title': 'Home'})

@login_required
def quiz(request):
    questions = Question.objects.all()
    options = Option.objects.all()
    correct_options = CorrectOption.objects.all()
    return render(request, 'quiz/quiz.html', {"Question": questions, "Option": options, "CorrectOption": correct_options})
