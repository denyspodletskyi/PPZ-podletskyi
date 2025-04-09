from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from .models import Question
from django.contrib.auth.forms import AuthenticationForm


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions': questions})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:question_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('polls:question_list')  # Після успішного логіну редірект на головну сторінку
    else:
        form = AuthenticationForm()

    return render(request, 'polls/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('polls:login')  # Перенаправлення на сторінку логіну


@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'polls/profile.html')
