from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Option, Question, CorrectOption, Assign
from django.contrib.auth.decorators import login_required
from django.db import connection
import random

def home(request):
    with connection.cursor() as cursor:
        # delete assigned questions to user using MySQL procedure `delete_assign`
        cursor.callproc('delete_assign', [request.user.id])
    assign_questions(request.user.id)
    return render(request, 'quiz/home.html', {'title': 'Home'})

def assign_questions(user_id, nquestions = 10):
    questions = Question.objects.all()
    for i in random.sample(range(1, len(questions)), nquestions):
        qid = questions[i].qid
        # assign question to user using MySQL procedure `insert_assign`
        with connection.cursor() as cursor:
            cursor.callproc('insert_assign', [user_id, qid])

@login_required
def quiz(request):
    assigned_questions = Assign.objects.filter(id = request.user.id)
    questions = []
    for q in assigned_questions:
        question = Question.objects.get(qid = q.qid)
        correct_options = CorrectOption.objects.filter(qid = q.qid)
        options = Option.objects.filter(qid = q.qid)
        questions.append({'question': question, 'options': options, 'correct_option': correct_options})

    return render(request, 'quiz/quiz.html', {'questions': questions})
