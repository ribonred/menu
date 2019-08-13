from decimal import Decimal
from django.conf import settings
from .models import product
class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    def tambah_produk(self, Product, quantity=1, update_quantity=False):
        Product_id = str(Product.id)
        if Product_id not in self.cart:
            self.cart[Product_id]={'quantity':0, 'price':str(Product.price)}
        if update_quantity:
            self.cart[Product_id]['quantity'] = quantity
        else:
            self.cart[Product_id]['quantity'] +=sum(quantity)
        self.save()
    def save(self):
        self.session.modified = True
    def remove(self, Product):
        Product_id = str(Product.id)
        if Product_id in self.cart:
            del self.cart[Product_id]
            self.save()
    def __iter__(self):
        Product_ids = self.cart.keys()
        products = product.objects.filter(id__in=Product_ids)

        cart = self.cart.copy()
        for Product in products:
            cart[str(Product.id)]['Product']= Product
        for item in cart.values():
            item['price']= Decimal(item['price'])
            item['total_price'] = item['price'] * item ['quantity']
            yield item
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    def get_total_harga(self):
        return sum(Decimal(item['price']) * item ['quantity'] for item in self.cart.values())
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    