from django import forms
from Authentication.models import User
from .models import Seller
from product.models import Product

class SellerRegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)
    name = forms.CharField(label="Name here", max_length=40, required=True)
    phone = forms.CharField(label="Phone Number", max_length=40, required=True)
    address = forms.CharField(label="Address", max_length=200)
    profile_pic = forms.ImageField(label="Upload Image")
    password1 = forms.CharField(label="Password", required=True)
    password2 = forms.CharField(label="Confirm Password", required=True)

    def clean(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Passwords dont match")
        return data
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.count()>0:
            raise forms.ValidationError("User with this email already exists")

        return email

    def clean_accepted_terms(self):
        if self.cleaned_data['accepted_terms'] != True:
            raise forms.ValidationError("You didn't accept our terms and conditions")
        return self.cleaned_data
    

    def save(self):
        data = self.cleaned_data
        email =  data['email']
        password = data['password1']
        user  = User.objects.create_seller_user(email=email,password=password)
        seller = Seller(
            user =user,
            name = data['name'],
            phone = data['phone'],
            address = data['address'],
            profile_pic = data['profile_pic'],

            )
        seller.save()

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        exclude = ['created_at' , 'updated_at']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fileds = '__all__'
        exclude = ['created_at' , 'updated_at']
        