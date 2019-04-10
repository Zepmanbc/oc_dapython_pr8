from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
        else:
            context['result'] = None
    return render(request, 'products/search.html', context)


def ResultView(request, product_id):
    context = {}
    result = []
    categories_list = Product.objects.get(pk=product_id).categories.values('id')
    toto = Product.objects.filter(nutrition_grades__gt='b')
    # recupérer tous les produits relatifs aux categories communes
    # les avoir une seule fois
    # supprimer celui qui fait référence
    # retirer ceux avec un nutrition grade inférieur
    # les ranger par ordre décroissant
    # en garder que 9 max
    

    # for category in categories_list:
    #     result.append(Product.objects.filter(categories=category[0]))
    

    if result:
        context['result'] = result
        context['query'] = result.product_name
    else:
        context['result'] = None
        context['query'] = 'Unknown'
    return render(request, 'products/search.html', context)


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
    return render(request, 'products/myproducts.html', context)
