from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from django.views.generic import ListView, DetailView

from .models import Product, Substitute
# Create your views here.


class SearchView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        return Product.objects.filter(product_name__icontains=self.request.GET['query'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.GET['query']
        context['target'] = 'products:result'
        return context


class ResultView(ListView):
    template_name = 'products/result.html'

    def get_queryset(self):
        self.product = Product.objects.get(pk=self.kwargs['product_id'])
        return Product.objects\
            .filter(category=self.product.category)\
            .filter(nutrition_grades__lte=self.product.nutrition_grades)\
            .exclude(id=self.kwargs['product_id'])\
            .order_by('nutrition_grades')[:9]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'allreadysaved' in self.request.GET:
            context['message'] = 'Déjà enregistré'
        context['query'] = self.product.product_name
        context['product'] = self.product
        context['title'] = self.product
        context['target'] = 'products:detail'
        return context


class DetailProductView(DetailView):
    template_name = 'products/detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = kwargs['object'].product_name
        return context

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
