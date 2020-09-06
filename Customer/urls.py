from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/' , signin , name="signin"),
    path('logout/',signout, name="signout"),
    path('<str:pk>/',customerpage ,name="customer-page"),
    path('register/',register ,name="register"),

]
