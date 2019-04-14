# from django.conf.urls import url
from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
     path('', TemplateView.as_view(template_name='products/index.html'), name='index'),
     path('legal', TemplateView.as_view(template_name='products/legal.html'), name='legal'),
     path('search/', views.SearchView.as_view(), name='search'),
     path('<int:product_id>/result/', views.ResultView.as_view(), name='result'),
     path('save/', views.SaveView, name='save'),
     path('delete/<int:pk>', views.DeleteSubstituteView.as_view(), name='delete'),
     path('<int:pk>/detail/', views.DetailProductView.as_view(), name='detail'),
     path('myproducts/', views.MyProductsView.as_view(), name='myproducts'),
]
