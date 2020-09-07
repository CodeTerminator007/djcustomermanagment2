from django.contrib import admin
from django.urls import path ,include
from Authentication.views import *
from Customer.views import customer_register , customer_products_view
from seller.views import seller_register

urlpatterns = [
    path('' , signin , name="signin"),
    path('customer_registeration/',customer_register ,name="customer_register"),
    path('seller_registeration/',seller_register ,name="seller_register"),
    path('products',customer_products_view ,name="customer_products"),
    path('logout/',signout, name="signout"),  
    path('seller/',include('seller.urls')),
    path('customer/',include('Customer.urls')),
    path('admin/', admin.site.urls),
]
