from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm, LoginForm
# from .models import User

# Create your views here.


# def LoginView(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(email=email, password=raw_password)
#             if user:
#                 login(request, user)
#                 return redirect('products:index')
#     else:
#         form = LoginForm()

#     return render(request, 'authentication/login.html', {'form': form})


def AccountView(request):
    if request.user.is_authenticated:
        fullname = " ".join([request.user.first_name, request.user.last_name])
        context = {'fullname': fullname}
        return render(request, 'authentication/account.html', context)
    else:
        return redirect('authentication:login')


@login_required
def LogoutView(request):
    logout(request)
    return redirect('products:index')


# def RegisterView(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()  # create user in DB

#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=raw_password)
#             login(request, user)

#             return redirect('products:index')
#     else:
#         form = RegisterForm()
#         return render(request, 'authentication/register.html', {'form': form})


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('products:index')
    template_name = 'authentication/register.html'


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('products:index')
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=raw_password)
        if user:
            login(self.request, user)
        return super().form_valid(form)
