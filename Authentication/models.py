from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin
from django.utils import timezone

ADMIN = 1
CUSTOMER = 2
USER_TYPE_CHOICES = (
    ('ADMIN' , 'Admin'),
    ('CUSTOMER' , 'Customer'),    
)
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_customer(self,**kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser =  False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def normalize_email(self, email):
        return email.lower()




class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField( max_length=255, unique=True)
    user_type = models.CharField(max_length=200,choices=USER_TYPE_CHOICES,null=True)
    last_login = models.DateTimeField( blank=True, null=True)


    is_staff = models.BooleanField( default=False)
    is_superuser = models.BooleanField( default=False)

    is_active = models.BooleanField( default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['email']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email