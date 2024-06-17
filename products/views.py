from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Category, Product

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            context['category'] = get_object_or_404(Category, slug=category_slug)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset.filter(available=True)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context