from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from quiz.models import Question
import random


def assign_questions(user_id, nquestions=10):
    """
    Assign `nquestions` random questions to user from the database of questions
    using the MySQL procedure `insert_assign`
    """
    questions = Question.objects.all()
    for i in random.sample(range(1, len(questions)), nquestions):
        qid = questions[i].qid
        with connection.cursor() as cursor:
            cursor.callproc("insert_assign", [user_id, qid])


def login_page(request):
    """
    Form for logging in user, authenticating user and redirect to home page after
    successful login. Also assigns questions to user and delete previously assigned
    questions.
    """
    form = LoginForm(request.POST or None)
    next_ = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("id")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            url_is_safe = url_has_allowed_host_and_scheme(
                url=redirect_path,
                require_https=request.is_secure(),
                allowed_hosts=request.get_host(),
            )
            # delete assigned questions to user using MySQL procedure `delete_assign`
            with connection.cursor() as cursor:
                cursor.callproc("delete_assign", [request.user.id])
            assign_questions(request.user.id)
            if url_is_safe and redirect_path:
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Invalid login")
            print(form.errors)
    return render(request, "users/login.html", {"form": form})


def register_page(request):
    """
    Form for registering new users and redirect to login page after successful
    registration.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("id")
            messages.success(request, "Account created for " + username)
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    """
    View for user profile.
    """
    return render(request, "users/profile.html")
