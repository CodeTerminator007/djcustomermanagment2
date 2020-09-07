from django.db import models
from Authentication.models import User
from seller.models import Seller    
from product.models import Product  
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)
    profile_pic = models.ImageField(null=True, default="defaultprofile.jpg" ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,max_length=200)
    updated_at = models.DateTimeField(auto_now=True,max_length=200)
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


    def __str__(self):
        return self.user.email


    def get_absolute_url(self):
        """Return absolute url for Student."""
        return ('')    

    
class Order(models.Model):
    STATUS = (
        ('Pending' , 'Pending'),
        ('Delivered' , 'Delivered'),
    )
    customer = models.ForeignKey(Customer , null=True , on_delete=models.SET_NULL) 
    product = models.ForeignKey(Product,null=True , on_delete=models.SET_NULL) 
    date_created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    def __str__(self):
        return self.product.name

