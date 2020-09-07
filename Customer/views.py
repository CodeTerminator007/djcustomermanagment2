from django.shortcuts import (
    render , HttpResponse ,
    redirect , Http404 )
    
from Authentication.models import User ,UserManager
from .models import Customer  ,Order
from product.models import Product
from .forms import CustomerRegistrationForm , OrderForm , CustomerForm  


def customer_home(request,pk):
    try:
        customer =  Customer.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404("User Does Not Exisit")
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {'customer':customer , 'orders':orders , "total_order":total_order }
    return render(request,"customer_home.html",context)


def customer_register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            customer =  Customer.objects.get(user__email=email)
            return redirect('customer-home' ,customer.id )
        else:
            return HttpResponse("Error in Form is  Not Valid")
    form = CustomerRegistrationForm()
    context = {'form':form}
    return render(request,'customer_register.html' ,context )

def customer_products_view(request):
    products = Product.objects.all()
    context = {'products':products}

    return render(request,'products.html',context)

def place_order(request ,pk):
    customer =  Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method =="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-home' , pk=pk)
    context = {'form' :  form ,}
    return render(request,'place_order.html' , context)

def update_order(request ,pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =="POST":
        form = OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('customer-home' , pk=pk)
    context = {'form' :  form ,}
    return render(request,'place_order.html' , context)    



def delete_order(request ,pk):
    customer =  Customer.objects.get(id=pk)
    item = Order.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('customer-home' ,customer.id )
    context = {'item':item}
    return render(request,'delete.html' ,context )    

def settings_user(request):
    customer = request.user.customer
    form =  CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()    
            
    context = {'form' : form }

    return render(request , 'settings_update.html' , context)