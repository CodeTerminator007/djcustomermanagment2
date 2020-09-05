from django.db import models
from Authentication.models import User
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        """Return absolute url for Student."""
        return ('')    

    
