from django import forms
from Authentication.models import User
from .models import Customer , Order
class CustomerRegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)
    first_name = forms.CharField(label="Fist Name", max_length=40, required=True)
    last_name = forms.CharField(label="Last Name", max_length=40, required=True)
    profile_pic = forms.ImageField(label="Upload Image")
    password1 = forms.CharField(label="Password", required=True)
    password2 = forms.CharField(label="Confirm Password", required=True)

    def clean_password1(self):
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
        user  = User.objects.create_customer_user(email=email,password=password)
        customer = Customer(
            user =user,
            first_name= data['first_name'],
            last_name = data['last_name'],
            profile_pic = data['profile_pic'],
            )
        customer.save()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fileds = '__all__'
        exclude = ['created_at' , 'updated_at']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['created_at' , 'updated_at']
        

