from django.contrib import admin
from django.urls import path ,include
from Authentication.views import *
from Customer.views import customer_register , customer_products_view
from seller.views import seller_register
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , signin , name="signin"),
    path('customer_registeration/',customer_register ,name="customer_register"),
    path('seller_registeration/',seller_register ,name="seller_register"),
    path('products',customer_products_view ,name="customer_products"),
    path('logout/',signout, name="signout"),  
    path('seller/',include('seller.urls')),
    path('customer/',include('Customer.urls')),
    path('404/',not_found,name='not_found'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

