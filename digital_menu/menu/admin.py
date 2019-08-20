from django.contrib import admin

# Register your models here.
from .models import product,Category, Order, OrderItem

class orderiteminline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['Product']
@admin.register(Order)
class orderadmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'no_tlp', 'created', 'updated', 'paid' ]
    list_filter = ['created', 'updated', 'paid']
    inlines = [orderiteminline]
@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(product)
class prodcutadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','tersedia','created','updated']
    list_filter = ['tersedia','created','updated', 'category']
    list_editable = ['price','tersedia']
    prepopulated_fields = {'slug': ('name',)}
