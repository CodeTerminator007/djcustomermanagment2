from django.contrib import admin
from django.urls import path
from .views import *
from Authentication.views import signin , signout

urlpatterns = [
    path('',customer_home ,name="customer-home"),
    path("order/",place_order ,name="place_order"),
    path('delete_order/<str:pk>',delete_order, name="delete_order"),
    path('settings_user/',settings_user, name="settings_user"),
    path('products/',customer_products_view, name="customer_products"),

]
