from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm
from .models import User

# Create your views here.


def LoginView(request, email, password):

    context = {'query': query}
    return render(request, 'products/search.html', context)

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


def SignInView(request, email, password):

    context = {
        'email': email,
        'password': password,
    }
    return render(request, 'products/search.html', context)
