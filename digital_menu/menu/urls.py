from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import productlist, produkdetail, cart_add, cart_remove, create_order

app_name ='menu'

urlpatterns = [
    path("", productlist.as_view(), name="home"),
    path("<slug:slug>/", productlist.as_view(), name="product_category"),
    url(r'^detail/(?P<slug>[\w-]+)$',produkdetail.as_view(), name='product_detail'),
    path("add/<int:Product_id>/", cart_add, name="addtocart"),
    path("remove/<int:Product_id>/", cart_remove, name="cart_remove"),
    path("order/create/", create_order, name="createorder"),
]