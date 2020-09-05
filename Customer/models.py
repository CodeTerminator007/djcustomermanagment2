from django.db import models
from django.contrib.auth import get_user_model
class Customer(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        """Return absolute url for Student."""
        return ('')    

    
