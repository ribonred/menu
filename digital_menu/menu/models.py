from django.db import models
from django.urls import reverse
from django.db.models import Sum
from django.db.models.signals import post_save
from django.conf import settings


# kategori
class Category(models.Model):
    name =  models.CharField(
        max_length = 80,
        db_index = True,
        null=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )
    class Meta:
        ordering = ('name',)
        verbose_name = ('category')
        verbose_name_plural = ('categories')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse("menu:product_category", kwargs=url_slug)
    
#model Product
class product(models.Model):
    category = models.ForeignKey(Category,
     related_name='products', 
     on_delete=models.CASCADE,
     null=True
     )
    name = models.CharField(max_length=255,db_index = True)
    slug = models.SlugField(max_length=255, db_index = True)
    image_product = models.ImageField(upload_to='product%y%m%d', blank=True)
    deskripsi = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    tersedia = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse("menu:product_detail", kwargs=url_slug)

##orderdetail

class Order(models.Model):
    nama = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class meta:
        ordering =('-created',)
    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_harga (self):
        return sum(item.get_cost() for item in self.item.all())
#barang yang di order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    Product = models.ForeignKey(product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity
