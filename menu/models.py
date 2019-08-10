from django.db import models
from django.urls import reverse

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
    harga = models.DecimalField(max_digits=12, decimal_places=0)
    tersedia = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse("menu:product_detail", kwargs=url_slug)

    def __str__(self):
        return self.name
    

