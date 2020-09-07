from django.shortcuts import (
    render , HttpResponse ,
    redirect , Http404 )
    
from Authentication.models import User ,UserManager
from .models import Customer
from .forms import CustomerRegistrationForm


def customer_home(request,pk):
    try:
        customer =  Customer.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404("User Does Not Exisit")

    context = {'customer':customer}
    return render(request,"customer_home.html",context)


def customer_register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            customer =  Customer.objects.get(user__email=email)
            return redirect('customer-page' ,customer.id )
        else:
            return HttpResponse("Error in Form is  Not Valid")
    form = CustomerRegistrationForm()
    context = {'form':form}
    return render(request,'customer_register.html' ,context )
