from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
            context['target'] = 'products:result'
        else:
            context['result'] = None
    return render(request, 'products/search.html', context)


def ResultView(request, product_id):
    context = {}
    if 'allreadysaved' in request.GET:
        context['message'] = "Déjà enregistré"
    result = []
    product = Product.objects.get(pk=product_id)

    result = Product.objects\
        .filter(category=product.category)\
        .filter(nutrition_grades__lte=product.nutrition_grades)\
        .exclude(id=product_id)\
        .order_by('nutrition_grades')[:9]

    if result:
        context['result'] = result
        context['query'] = product.product_name
        context['product'] = product
        context['target'] = 'products:detail'
    else:
        context['result'] = None
        context['query'] = 'Unknown'
    return render(request, 'products/result.html', context)


def DetailView(request, product_id):
    context = {}
    product = Product.objects.get(pk=product_id)
    context['query'] = product.product_name
    context['product'] = product

    return render(request, 'products/detail.html', context)


def LegalView(request):
    context = {}
    return render(request, 'products/legal.html', context)


@login_required
def SaveView(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        substitute_id = request.POST['substitute_id']
        next_url = request.POST['next']
        product_obj = Product.objects.get(pk=product_id)
        substitute_obj = Product.objects.get(pk=substitute_id)
        user_obj = User.objects.get(pk=request.user.id)
        # test if all obj are sets
        if product_obj and substitute_obj and user_obj:
            obj, created = Substitute.objects.get_or_create(
                user_id=user_obj,
                product_id=product_obj,
                substitute_id=substitute_obj
                )
            if created:
                return redirect('products:myproducts')
            else:
                return redirect(next_url+"?allreadysaved")
    return redirect('products:index')


@login_required
def MyProductsView(request):
    context = {}
    user_obj = User.objects.get(pk=request.user.id)
    substitute_list = Substitute.objects.filter(user_id=user_obj.id).order_by('-id')
    context['substitute_list'] = substitute_list
    context['title'] = 'mes produits'
    return render(request, 'products/myproducts.html', context)


@login_required
def DeleteView(request):
    if request.method == 'POST':
        substitute_id = request.POST['substitute_id']
        subst_obj = Substitute.objects.get(pk=substitute_id)
        subst_obj.delete()
        return redirect('products:myproducts')
    return redirect('products:index')
