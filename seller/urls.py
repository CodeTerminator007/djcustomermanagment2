from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('<str:pk>/',seller_home ,name="seller-home"),
    path("product/<str:pk>/",place_product ,name="place_product"),
    path('settings_seller/<str:pk>',settings_seller, name="settings_seller"),

]
