from django.contrib import admin
from django.urls import path
from .views import *
from Authentication.views import signin , signout

urlpatterns = [
    path('<str:pk>/',customer_home ,name="customer-page"),

]
