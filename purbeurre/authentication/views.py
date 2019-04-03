from django.shortcuts import render

# Create your views here.


def LoginView(request, email, password):

    context = {'query': query}
    return render(request, 'products/search.html', context)


def LogoutView(request):

    context = {}
    return render(request, 'products/search.html', context)


def RegisterView(request, email, password, name):

    context = {
        'email': email,
        'password': password,
        'name': name,
    }
    return render(request, 'products/search.html', context)
