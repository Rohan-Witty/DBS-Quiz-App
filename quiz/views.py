from django.shortcuts import render, redirect
from quiz.models import Option, Question, CorrectOption, Assign, Leaderboard
from django.contrib.auth.decorators import login_required
from .forms import Quiz


def home(request):
    """
    View for home page
    """
    leaderboard = Leaderboard.objects.all()
    return render(
        request, "quiz/home.html", {"title": "Home", "leaderboard": leaderboard}
    )


@login_required
def quiz(request):
    """
    View for quiz page
    """
    assigned_questions = Assign.objects.filter(id=request.user.id)
    questions = []
    for q in assigned_questions:
        question = Question.objects.get(qid=q.qid)
        correct_options = CorrectOption.objects.filter(qid=q.qid)
        options = Option.objects.filter(qid=q.qid)
        questions.append(
            {
                "question": question,
                "options": options,
                "correct_option": correct_options,
            }
        )
    form = Quiz(request.POST or None, questions=questions)
    if form.is_valid():
        form.save(request.user.id)
        return redirect("/")
    else:
        print(form.errors)
    return render(request, "quiz/quiz.html", {"title": "Quiz", "form": form})
