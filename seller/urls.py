from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('<str:pk>/',seller_home ,name="seller-home"),
    path("product/<str:pk>/",place_product ,name="place_product"),
    path('update_product/<str:pk>' , update_product ,name='update_product'),
    path('orders/<str:pk>' ,seller_orders_view ,name='seller-orders'),
    path('settings_seller/<str:pk>',settings_seller, name="settings_seller"),

]
