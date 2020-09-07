from django.contrib import admin
from django.urls import path
from .views import *
from Authentication.views import signin , signout

urlpatterns = [
    path('<str:pk>/',customer_home ,name="customer-home"),
    path("order/<str:pk>/",place_order ,name="place_order"),
    path('update_order/<str:pk>' , updae_order ,name='updae_order')

]
