from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm

# Create your views here.


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


class RegisterView(generic.FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('products:index')
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        if user:
            login(self.request, user)
        return super().form_valid(form)
