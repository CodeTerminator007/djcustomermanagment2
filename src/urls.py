from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('customer/',include('Customer.urls')),
    path('admin/', admin.site.urls),
]
