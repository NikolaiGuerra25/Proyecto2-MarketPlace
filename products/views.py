from django.shortcuts import render
from .models import Product, Reviews
from .forms import ReviewForm
from categorias.models import Categoria
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        categoria_slug = self.kwargs['categoria_slug']
        categoria = Categoria.objects.get(slug=categoria_slug)
        return Product.objects.filter(categoria=categoria)

class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'productCreate.html'
    fields = ['name', 'description', 'price', 'category', 'imagen']

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        messages.success(self.request, 'Producto agregado con exito')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('categorias:categoryList')
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'productDetail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object  
        reviews = Reviews.objects.filter(product=product)  
        context['reviews'] = reviews
        return context



class reviewCreateView(generic.CreateView):
    model = Reviews
    template_name = 'review.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
     context = super(reviewCreateView, self).get_context_data(**kwargs)
     context['product'] = Product.objects.get(slug=self.kwargs['nombre_producto'])
     print(context['product'])
     return context
    
    def form_valid(self, form):
        form.instance.product= Product.objects.get(slug=self.kwargs['nombre_producto'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('categorias:categoryList')

class reviewListView(generic.ListView):
    model = Reviews
    template_name = 'productDetail.html'
    context_object_name = 'reviews'
