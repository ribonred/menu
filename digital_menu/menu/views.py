from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import formtambahproduk
from .models import product,Category

class productlist(ListView):
    template_name = "index.html"
    context_object_name = 'Product' #context temmplate
    
    def get_queryset(self):
        queryset = product.objects.all() #overide context dengan model product
        if 'slug' in self.kwargs: #jika url memanggil slug e.g: localhost/slug
            category = get_object_or_404(Category, slug=self.kwargs['slug']) #mengambil model category slug
            queryset = product.objects.filter(category__name=category.name) #filter produk dengan slug berdasarkan nama category
        return queryset #overide context dengan object product terfilter
    def get_context_data(self, **kwargs):
        context = super(productlist, self).get_context_data(**kwargs)
        context['kategoris'] = Category.objects.all()  #penambahan model category
        context['jumlah_form'] = formtambahproduk()
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

@require_POST
def cart_add(request, Product_id):
    cart = Cart(request)
    Product = get_object_or_404(product, id=Product_id)
    form = formtambahproduk(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.tambah_produk(Product=Product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('menu:cart_detail')

def cart_remove(request, Product_id):
    cart = Cart(request)
    Product = get_object_or_404(product, id=Product_id)
    cart.remove(Product)
    return redirect('menu:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart':cart})

