from django.db import models
from seller.models import Seller

class Product(models.Model):
    seller = models.ForeignKey(Seller , on_delete=models.CASCADE)
    name = models.CharField(unique=True,max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,max_length=200)
    updated_at = models.DateTimeField(auto_now=True,max_length=200)


    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

