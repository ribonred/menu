from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, reverse
from .models import product,Category

class productlist(ListView):
    template_name = "home.html"
    context_object_name = 'produk' #context temmplate
    
    def get_queryset(self):
        queryset = product.objects.all() #overide context dengan model product
        if 'slug' in self.kwargs: #jika url memanggil slug e.g: localhost/slug
            category = get_object_or_404(Category, slug=self.kwargs['slug']) #mengambil model category slug
            queryset = product.objects.filter(category__name=category.name) #filter produk dengan slug berdasarkan nama category
        return queryset #overide context dengan object product terfilter
    def get_context_data(self, **kwargs):
        context = super(productlist, self).get_context_data(**kwargs)
        context['kategoris'] = Category.objects.all() #penambahan model category
        return context
    
class produkdetail(DetailView):
    model = product
    template_name = 'detail.html'
    slug_field = 'slug'
    context_object_name = 'produk'
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['kategoris'] = Category.objects.all() #penambahan model category
        return context