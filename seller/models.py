from django.db import models
from Authentication.models import User , UserManager

class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=60,null=True)
    phone = models.CharField(max_length=13,null=True)
    created_at = models.DateTimeField(auto_now_add=True,max_length=200)
    updated_at = models.DateTimeField(auto_now=True,max_length=200)    
    class Meta:

        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.user.email
