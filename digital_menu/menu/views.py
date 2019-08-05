from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, reverse
from .models import product,category

class productlist(ListView):
    model = product
    template_name = "home.html"
    context_object_name = 'produk'
    def get_context_data(self, **kwargs):
        context = super(productlist, self).get_context_data(**kwargs)
        context['kategori'] = category.objects.all
        return context
class produkdetail(DetailView):
    model = product
    template_name = 'detail.html'