from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',seller_home ,name="seller-home"),
    path("product/",place_product ,name="place_product"),
    path('update/<str:pk>' , update_product ,name='update_product'),
    path('orders/<str:pk>' ,seller_orders_view ,name='seller-orders'),
    path('settings/',settings_seller, name="settings_seller"),

]
