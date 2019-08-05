from django.contrib import admin

# Register your models here.
from .models import product,category

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(product)
class prodcutadmin(admin.ModelAdmin):
    list_display = ['name','slug','harga','tersedia','created','updated']
    list_filter = ['tersedia','created','updated']
    list_editable = ['harga','tersedia']
    prepopulated_fields = {'slug': ('name',)}