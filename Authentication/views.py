from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from .models import *
from Customer.models import Customer

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        print(email)
        print(password)
        print(user)

        
        if user is not None :            
            login(request,user)
            if user.user_type == "CUSTOMER":
                customer =  Customer.objects.get(user__email=user.email)
                return redirect('customer-page' , customer.id)
            if user.user_type == "SELLER":
                seller = Seller.objects.get(user__email=user.email) 
                return redirect ('customer-page', seller.id)              
        else:
            pass
    return render(request , 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')