from django.contrib import admin

# Register your models here.
from .models import product,Category

@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(product)
class prodcutadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','tersedia','created','updated']
    list_filter = ['tersedia','created','updated']
    list_editable = ['price','tersedia']
    prepopulated_fields = {'slug': ('name',)}
