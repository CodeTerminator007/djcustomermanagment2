from django.shortcuts import (
    render , HttpResponse ,
    redirect , Http404 )
    
from Authentication.models import User ,UserManager
from .models import Customer  ,Order
from django.contrib.auth.decorators import user_passes_test ,login_required 
from product.models import Product
from .forms import CustomerRegistrationForm , OrderForm , CustomerForm  


def is_user_customer(user):

    if user.is_authenticated :
        if user.user_type=="CUSTOMER":
            return user
            
@user_passes_test(is_user_customer , login_url='signin')
def customer_home(request):
    try:
        customer =  Customer.objects.get(user=request.user)
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
            return redirect('signin' )
        
    form = CustomerRegistrationForm()
    context = {'form':form}
    return render(request,'customer_register.html' ,context )

@login_required(login_url="signin")
@user_passes_test(is_user_customer , login_url='signin')
def customer_products_view(request):
    products = Product.objects.all()
    context = {'products':products}

    return render(request,'products.html',context)

@login_required(login_url="signin")
@user_passes_test(is_user_customer , login_url='signin')
def place_order(request):
    customer =  Customer.objects.get(user=request.user)
    form = OrderForm(initial={'customer':customer})
    if request.method =="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-home')
    context = {'form' :  form ,}
    return render(request,'place_order.html' , context)


# @login_required(login_url="signin")
# @user_passes_test(is_user_customer , login_url='signin')
# def update_order(request ,pk):

#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)
#     if request.method =="POST":
#         form = OrderForm(request.POST , instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('customer-home' , pk=pk)
#     context = {'form' :  form ,}
#     return render(request,'place_order.html' , context)    

@login_required(login_url="signin")
@user_passes_test(is_user_customer , login_url='signin')
def delete_order(request,pk):
    item = Order.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('customer-home'  )
    context = {'item':item}
    return render(request,'delete.html' ,context )    


@login_required(login_url="signin")
@user_passes_test(is_user_customer , login_url='signin')
def settings_user(request):
    customer =  Customer.objects.get(user=request.user)
    form =  CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()    
            
    context = {'form' : form ,"customer":customer}

    return render(request , 'settings_update.html' , context)