from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from quiz.models import Question
import random

# Create your views here.

# assign question to user using MySQL procedure `insert_assign`
def assign_questions(user_id, nquestions = 10):
    questions = Question.objects.all()
    for i in random.sample(range(1, len(questions)), nquestions):
        qid = questions[i].qid
        with connection.cursor() as cursor:
            cursor.callproc('insert_assign', [user_id, qid])

def login_page(request):
    form = LoginForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            url_is_safe = url_has_allowed_host_and_scheme(
                url = redirect_path,
                require_https = request.is_secure()
            )
            # delete assigned questions to user using MySQL procedure `delete_assign`
            with connection.cursor() as cursor:
                cursor.callproc('delete_assign', [request.user.id])
            assign_questions(request.user.id)
            print("assigned questions to user: " + request.user.id)
            if url_is_safe and redirect_path:
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Invalid login")
            print(form.errors)
    else:
        print("Error")
    return render(request, "users/login.html", { "form": form })

User = get_user_model()

def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('id')
            messages.success(request, "Account created for " + username)
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    return render(request, "users/profile.html")