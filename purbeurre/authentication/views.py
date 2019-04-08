from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm
from .models import User

# Create your views here.


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})

@login_required
def LogoutView(request):

    context = {}
    return render(request, 'products/search.html', context)


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # create user in DB

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)

            return redirect('logout')
    else:
        form = RegisterForm()
        return render(request, 'authentication/register.html', {'form': form})
