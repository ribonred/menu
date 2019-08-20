from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import formtambahproduk, formupdateproduk, orderform
from .models import product,Category, Order,OrderItem
from django.contrib import messages
from django.http import JsonResponse

class productlist(ListView):
    template_name = "index.html"
    context_object_name = 'Product' #context temmplate
    paginate_by = 5 #berapa object yang di tampilkan
    
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
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        for item in cart:
            item['quantity_form'] = formupdateproduk(
            initial={'quantity': item['quantity'],
            'update': True})
        return super().get(request, *args, **kwargs)
    
class produkdetail(DetailView):
    model = product
    template_name = 'snippets/prodetail.html'
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
        messages.success(request, 'Menu di tambahkan ke keranjang')
        return redirect('menu:home')

def cart_remove(request, Product_id):
    cart = Cart(request)
    Product = get_object_or_404(product, id=Product_id)
    cart.remove(Product)
    return redirect('menu:home')

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = orderform(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, Product=item['Product'], price=item['price'], quantity=item['quantity'])
                cart.clear()
                return render (request, 'createdorder.html', {'order':order})
    else:
        form = orderform()
        return render(request, 'createorder.html', {'form':form})



