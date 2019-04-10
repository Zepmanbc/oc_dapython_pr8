from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Substitute
# Create your views here.


def IndexView(request):

    context = {}
    return render(request, 'products/index.html', context)


def SearchView(request):
    context = {}
    if request.method == 'GET':
        query = request.GET['query']
        context['query'] = query
        result = Product.objects.filter(product_name__icontains=query)
        if result:
            context['result'] = result
            context['title'] = query
        else:
            context['result'] = None
    return render(request, 'products/search.html', context)


def ResultView(request, product_id):
    context = {}
    result = []
    curr_product = Product.objects.get(pk=product_id)

    result = Product.objects\
        .filter(category=curr_product.category)\
        .filter(nutrition_grades__lte=curr_product.nutrition_grades)\
        .exclude(id=product_id)\
        .order_by('nutrition_grades')[:9]

    if result:
        context['result'] = result
        context['query'] = curr_product.product_name
        context['curr_product'] = curr_product
    else:
        context['result'] = None
        context['query'] = 'Unknown'
    return render(request, 'products/result.html', context)


def DetailView(request, product_id):
    context = {}
    return render(request, 'products/detail.html', context)


def LegalView(request):

    context = {}
    return render(request, 'products/legal.html', context)


def SaveView(request, product_id, substitude_id):

    context = {}
    return render(request, 'products/index.html', context)


@login_required
def MyProductsView(request):
    context = {}
    context['title'] = 'mes produits'
    return render(request, 'products/myproducts.html', context)
