from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('<str:pk>/',seller_home ,name="seller-home"),

]
