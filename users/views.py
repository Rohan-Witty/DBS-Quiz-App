from email import message
from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.http import url_has_allowed_host_and_scheme
# from quiz.mixins import NextUrlMixin, RequestFormAttachMixin
from django.views.generic import CreateView, FormView
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
#     form_class = LoginForm
#     success_url = '/'
#     template_name = 'accounts/login.html'
#     default_next = '/'

#     def form_valid(self, form):
#         next_path = self.get_next_url()
#         return redirect(next_path)

# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = 'accounts/register.html'
#     success_url = '/login/'

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_path,
            require_https=request.is_secure(),
            )
            if url_is_safe and redirect_path:
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, "users/login.html", context)


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