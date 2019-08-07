from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import productlist,produkdetail

app_name ='menu'

urlpatterns = [
    path("", productlist.as_view(), name="home"),
    path("category/<slug:slug>/", productlist.as_view(), name="product_category"),
    url(r'^detail/(?P<slug>[\w-]+)$',produkdetail.as_view(), name='product_detail'),
]