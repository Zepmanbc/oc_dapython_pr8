from django.shortcuts import render
# Create your views here.


def IndexView(request):

    context = {}
    return render(request, 'products/index.html', context)


def SearchView(request, query):

    context = {'query': query}
    return render(request, 'products/search.html', context)


def DetailView(request, product_id):

    context = {}
    return render(request, 'products/detail.html', context)


def ResultView(request, product_id):

    context = {}
    return render(request, 'products/result.html', context)


def LegalView(request):

    context = {}
    return render(request, 'products/legal.html', context)


def SaveView(request, product_id, substitude_id):

    context = {}
    return render(request, 'products/index.html', context)


def MyProductsView(request):

    context = {}
    return render(request, 'products/myproducts.html', context)
